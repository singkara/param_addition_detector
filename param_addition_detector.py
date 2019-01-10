from pydriller import RepositoryMining, GitRepository

def get_parent_commit_objects(commit, repositoryPath):
    '''
    Given a commit object, this function returns the parent commits
    :param commit:
    :return: Parent Commit objects (2 in case of merge commit)
    '''
    parentCommitHashes = commit.parents
    parentCommits=[]
    for parentCommitHash in parentCommitHashes:
        parentCommitGenerator = RepositoryMining(repositoryPath,single=parentCommitHash).traverse_commits()
        for parentCommit in parentCommitGenerator:
            parentCommits.append(parentCommit)
    return parentCommits


def get_method_parameter_count(commit, file, originalMethodName):
    '''
    This function returns the parameter count and the method signature.
    :param commit:
    :param file:
    :param originalMethodName:
    :return: Tuple containing parameter count and method name
    '''
    parameterCount = -1
    longMethodName = 'Not Found'

    for modifiedFile in commit.modifications:
        if (modifiedFile.filename == file.filename):
            for method in modifiedFile.methods:
                if method.name == originalMethodName:
                    parameterCount= len(method.parameters)
                    longMethodName=method.long_name
    return (parameterCount,longMethodName)




def main():

    print("Enter relative path to the repository:")
    repositoryPath=input()

    print("Enter the name of the output csv file")
    csvFileName= input()
    file = open(csvFileName,"w")
    file.write("Commit SHA, Java File, Old function signature, New function signature \n")

    #Get git repository
    gr= GitRepository(repositoryPath)
    #Get all commits
    allCommits=RepositoryMining(repositoryPath).traverse_commits()
    # Open csv to write the output

    for commit in allCommits:

        #Fetch parent commits to compare method parameters
        parentCommits= get_parent_commit_objects(commit,repositoryPath)


        for modified_file in commit.modifications:

            #get added code and removed code for this commit and this file
            parsed_diff= gr.parse_diff(modified_file.diff)
            addedCodeInFile= ''.join([x[1] for x in parsed_diff["added"]])
            removedCodeInFile= ''.join([x[1] for x in parsed_diff["deleted"]])


            for method in modified_file.methods:
                methodName= method.name.split('::', 1)[-1]

                # If the method exists in both added and removed code, it is modified.
                if methodName in addedCodeInFile and methodName in removedCodeInFile:
                    # Get Param Count and Signature
                    parameter_count,signature= get_method_parameter_count(commit, modified_file ,method.name)
                    # Get its Parent's Param Count and Signature
                    parent_parameter_count,parent_commit_signature = get_method_parameter_count(min(parentCommits,key=lambda x: get_method_parameter_count(x, modified_file, method.name)[0]),modified_file,method.name)

                    #Compare if Child has more parameters than its parent- If yes, log it to file and console
                    if(parameter_count > parent_parameter_count and signature != "Not Found" and parent_commit_signature != "Not Found"):
                        print(commit.hash+","+ modified_file.filename+","+ parent_commit_signature+ "," + signature)
                        file.write(commit.hash+","+ modified_file.filename+","+ parent_commit_signature+ "," + signature+"\n")

    print("Process Completed Successfully!")


if __name__ == '__main__':
    main()