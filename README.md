# Python source code obfuscation

**Author**: Bc. Adrián Ondov

**Subject**: Bezpečnosť informačných technológií

**Academic year**: 2022/2023

---

## **Disclaimer**

It is highly recommended to review the source code before running the script, and also to run the script via the command line, not by running the .exe file (it might not work). The encryption mechanism isn’t currently set to any folder path, therefore it is important to change it to test its functionality. Even though there is a decryption function present in the repository, it is still dangerous to encrypt your files without any reason to do so. 

To change the path, which should be encrypted, search for the command ”os.chdir(<path>)” (located at the top of the script) and change the path. When changing the path in the PyArmor encryption script, it is required to change the path in the original encryption.py file and then obfuscate it using a simple command described in section 4.2.1 (see the documentation).

Also, it is important to run the decryption script from the folder, where the encrypt key is located, or it won’t be able to decrypt any files.

---

## Assignment

Data obfuscation can pose a serious problem when trying to secure the user’s devices against malware. Even though modern anti-malware programs are slowly being adjusted to detect such hiding methods, some new obfuscation methods are difficult to uncover. End devices could therefore become infected with malware without knowing it. Regardless of its malicious use, the best defense against these attacks is to know how to identify if they are present and possibly mitigate them. The goal of the first part of this assignment is to analyze existing methods of source code obfuscation used in Python code (e.g. PyArmor).

After analysis, at least three methods should be implemented into a simple Python script, with the addition of documenting all of the changes that were made to code after the obfuscation process (e.g. how it changed visually or logically). The second part should be focused on testing the introduced methods of source code obfuscation against the existing static dynamic code analysis tools (e.g. VirusTotal). The functionality of used techniques should also be properly described. The whole process should be properly documented to find out the effectiveness of chosen source code obfuscation methods and to see if the applied countermeasures will be successful in detecting them.

Goals of the project consist of several points:
- Analyze existing methods of source code obfuscation.
- Write a simple program in Python and use it to implement at least three methods described in the analysis.
- Test the obfuscation methods against the existing static/dynamic code analysis tool (e.g. VirusTotal).
- Specify the effectiveness of used obfuscation methods.
- Present the theoretical, as well as the practical findings discovered during the creative process.

The output of this assignment should be a document, where each goal from the section above will be described. It should be divided into theoretical and practical parts. Additionally, a Python script created as a sample for obfuscation should be submitted as well. In the practical part, a graphical representation of results should be present as much as possible. The assumed length of the document should be approximately 7-10 pages (images not included).

---

## Repository layout

In this repository, all of the Python files can be found, including the original script, which allows using a decryption function (the password is located in the source code).

Each method is divided into a separate folder, which includes the obfuscated encrypt.py file and its executable form. Executable files can be found on the path **”/EXE/dist/encrypt.exe”** (applies to each method folder). Executable files can be used only for the VirusTotal scanning purposes, since it does not work correctly when trying to run the encryption process.
