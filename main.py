import os
import re
import shutil


rootDir = "/Users/ife/Documents/Android_Studio_Projects/AndroidProjectTemplateCopy"
userDefinedPackageName = "one.two.three.cheese"
listOfTargetFolders = ["main", "test", "androidTest"]

def dumpFileTree():
    for root, dirs, files in os.walk(rootDir):
        print(f"(dirs: {dirs}, files: {files})")

def walkFromSourceDirectory(source):
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

def renamePackageNameInFiles(dotNotationPackageName):

    defaultPackageName = "com.ife.android_project_template"
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

def createFreshDirectories(sourceFolder, destinationFolder, deleteComFolderFor):
    print(f"Creating path: {destinationFolder}")
    os.makedirs(destinationFolder, exist_ok=True)
    for item in os.scandir(sourceFolder):
        s = os.path.join(sourceFolder, item.name)
        d = os.path.join(destinationFolder, item.name)
        if item.is_file():
            shutil.copy2(s, d)
        elif item.is_dir():
            shutil.copytree(s, d, ignore_dangling_symlinks=True, dirs_exist_ok=True)

    # Delete the /com folder
    print(f"Deleting /com folder for app/src/{deleteComFolderFor}")
    shutil.rmtree(os.path.join(rootDir, f"app/src/{deleteComFolderFor}/java/com"))

def feedTargetFoldersForCreation(listOfFolders, dotNotationPackageName):
    for folder in listOfFolders:
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
    dotNotationPackageName = userDefinedPackageName
)



# dumpFileTree()
# listKotlinGradleAndTomlFiles()
# walkFromSourceDirectory("/Users/ife/Documents/Android_Studio_Projects/AndroidProjectTemplateCopy/app/src")
