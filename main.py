import argparse
import os
import shutil
import sys

# rootDir = "/Users/ife/Documents/Android_Studio_Projects/AndroidProjectTemplateCopy"
rootDir = "../"

defaultPackageName = "com.ife.android_project_template"
defaultProjectName = "MyAndroidProjectTemplate"
parser = argparse.ArgumentParser(description = "")
parser.add_argument("packageName", type=str, help="The package name in dot notation.", default=defaultPackageName)
parser.add_argument("projectName", type=str, help="The project name", default=defaultProjectName)
args = parser.parse_args()

userDefinedPackageName:str = args.packageName # e.g one.two.three.cheese
projectName = args.projectName

packagePrefixTriggered:bool = False

listOfTargetFolders = ["main", "test", "androidTest"]

def dumpFileTree():
    for root, dirs, files in os.walk(rootDir):
        print(f"(dirs: {dirs}, files: {files})")

def walkFromSourceDirectory(source):
    print(f"Directory walk from {source}")
    for root, dirs, files in os.walk(source):
        for dir in dirs:
            print(os.path.join(root, dir))

def listKotlinGradleAndTomlFiles():
    listOfKotlinFiles = []
    listOfPureGradleFiles = []
    listOfKotlinGradleFiles = []
    projectTomlConfigFile = ""

    for root, dirs, files in os.walk(rootDir):
        for file in files:
            if file.endswith(".kt"):
                kotlinFilePath = os.path.join(root, file)
                listOfKotlinFiles.append(kotlinFilePath)

            if file.endswith(".gradle"):
                pureGradlePath = os.path.join(root, file)
                listOfPureGradleFiles.append(pureGradlePath)

            if file.endswith(".gradle.kts"):
                kotlinGradlePath = os.path.join(root, file)
                listOfKotlinGradleFiles.append(kotlinGradlePath)

            if file.endswith("myproject.config.toml"):
                projectTomlConfigFile = os.path.join(root, file)


    print(f'Found kotlin files ', end="\n")
    for file in listOfKotlinFiles:
        print(file)
    print("")

    print(f'Found pure gradle files ', end="\n")
    for file in listOfPureGradleFiles:
        print(file)
    print("")

    print(f'Found kotlin gradle files ', end="\n")
    for file in listOfKotlinGradleFiles:
        print(file)
    print("")

    print(f'Found project toml config file ', end="\n")
    print(projectTomlConfigFile)
    print("")

def renamePackageNameInFiles(dotNotationPackageName, userDefinedProjectName):

    # defaultPackageName = "com.ife.android_project_template"
    # defaultProjectName = "AndroidProjectTemplate"
    kotlin_package_name_to_search = f"package {defaultPackageName}"
    importsToSearch = f"import {defaultPackageName}"

    for root, dirs, files in os.walk(rootDir):
        for file in files:

            if file.endswith(".kt"):
                kotlinFilePath = os.path.join(root, file)

                with open(kotlinFilePath, 'r') as f:
                    file_contents = f.read()

                    if kotlin_package_name_to_search in file_contents:
                        file_contents = file_contents\
                            .replace(kotlin_package_name_to_search, f'package {dotNotationPackageName}')

                        file_contents = file_contents\
                            .replace(importsToSearch, f'import {dotNotationPackageName}')

                        print(f"Renamed package name and imports in {kotlinFilePath} with {dotNotationPackageName}")

                        with open(kotlinFilePath, 'w') as f:
                            f.write(file_contents)

            if file.endswith("myproject.config.toml"):
                projectTomlConfigFile = os.path.join(root, file)

                with open(projectTomlConfigFile, 'r') as f:
                    file_contents = f.read()

                    if defaultPackageName in file_contents:
                        file_contents = file_contents.replace(defaultPackageName, dotNotationPackageName)

                        print(f"Renamed package name in {projectTomlConfigFile} with {dotNotationPackageName}")

                        with open(projectTomlConfigFile, 'w') as f:
                            f.write(file_contents)

            if file.endswith(".kts"):
                gradleFile = os.path.join(root, file)

                with open(gradleFile, 'r') as f:
                    file_contents = f.read()

                    if defaultPackageName in file_contents:
                        file_contents = file_contents.replace(defaultPackageName, dotNotationPackageName)
                        print(f"Renamed package name in {gradleFile} with {dotNotationPackageName}")

                        with open(gradleFile, 'w') as f:
                            f.write(file_contents)

                    if defaultProjectName in file_contents:
                        file_contents = file_contents.replace(defaultProjectName, userDefinedProjectName)
                        print(f"Renamed project name in {gradleFile} with {userDefinedProjectName}")

                        with open(gradleFile, 'w') as f:
                            f.write(file_contents)

            if file.endswith(".xml"):
                xmlFile = os.path.join(root, file)

                with open(xmlFile, 'r') as f:
                    file_contents = f.read()

                    if defaultProjectName in file_contents:
                        file_contents = file_contents.replace(defaultProjectName, userDefinedProjectName)
                        print(f"Renamed app_name string in {xmlFile} with {userDefinedProjectName}")

                        with open(xmlFile, 'w') as f:
                            f.write(file_contents)

def createFreshDirectories(sourceFolder:str, destinationFolder:str, deleteComFolderFor:str):
    print(f"Creating path: {destinationFolder}")

    os.makedirs(destinationFolder, exist_ok=True)
    for item in os.scandir(sourceFolder):
        s = os.path.join(sourceFolder, item.name)
        d = os.path.join(destinationFolder, item.name)
        if item.is_file():
            shutil.copy2(s, d)
        elif item.is_dir():
            shutil.copytree(s, d, ignore_dangling_symlinks=True, dirs_exist_ok=True)

    # Delete the original /com path as its not needed
    print(f"Deleting /com folder for app/src/{deleteComFolderFor}")
    com_folder = os.path.join(rootDir, f"app/src/{deleteComFolderFor}/java/com")
    if os.path.isdir(com_folder) and 'android_project_template' in os.listdir(com_folder):
        shutil.rmtree(com_folder)
        print(f"Deleting {com_folder}")

    shutil.rmtree(os.path.join(rootDir, f"app/src/{deleteComFolderFor}/java/com"))
    print(f"Deleted the com folder --> app/src/{deleteComFolderFor}/java/com")

    # Rename destination folder to remove the "mycom" prefix to change it to start with "com" instead
    # if packagePrefixTriggered:
    #     print("Renaming `mycom` to `com`")
    #
    #     newPathName = destinationFolder.replace("mycom", "com")
    #
    #     print(f"Destination path ({destinationFolder}) exists? {os.path.exists(destinationFolder)} ")
    #     print(f"New path exists? {os.path.exists(newPathName)} ")
    #
    #     # New Path should not exist yet because it's not been created yet.
    #     print(f"Destination path: {destinationFolder}")
    #     print(f"New path: {newPathName}")
    #
    #     # os.rename(
    #     #     destinationFolder,
    #     #     newPathName
    #     # )
    #
    #     os.rename(
    #         os.path.join(destinationFolder),
    #         os.path.join(newPathName)
    #     )

def feedTargetFoldersForCreation(listOfFolders, dotNotationPackageName):
    # if the package name starts with com then replace it with a prefix
    if dotNotationPackageName.split(".")[0] == "com":
        global packagePrefixTriggered
        packagePrefixTriggered = True
        dotNotationPackageName = dotNotationPackageName.replace("com", "mycom")

    for folder in listOfFolders:
        print(f"folder -> {folder}")
        # src_folder = os.path.join(rootDir, f"app/src/main/java/com/ife/android_project_template")
        src_folder = os.path.join(rootDir, f"app/src/{folder}/java/com/ife/android_project_template")
        # dst_folder = os.path.join(rootDir, f"app/src/main/java/one.two.three.cheese)
        dst_folder = os.path.join(rootDir, f"app/src/{folder}/java/{dotNotationPackageName.replace('.', os.sep)}")
        createFreshDirectories(sourceFolder = src_folder, destinationFolder = dst_folder, deleteComFolderFor = folder)


feedTargetFoldersForCreation(
    listOfFolders = listOfTargetFolders,
    dotNotationPackageName = userDefinedPackageName
)

renamePackageNameInFiles(
    dotNotationPackageName = userDefinedPackageName,
    userDefinedProjectName = projectName
)



# dumpFileTree()
# listKotlinGradleAndTomlFiles()
# walkFromSourceDirectory("/Users/ife/Documents/Android_Studio_Projects/AndroidProjectTemplateCopy/app/src")
