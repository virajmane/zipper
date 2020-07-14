import zipfile, os

def zipfiles(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + "_" +str(number) +".zip"
        if not os.path.exists(zipFileName):
            break
        number += 1

    print("Creating %s..." %(zipFileName))
    zipping = zipfile.ZipFile(zipFileName, "w")
    for foldername,subfolders,filenames in os.walk(folder):
        print("Adding files %s" %(foldername))
        zipping.write(foldername)
        for filename in  filenames:
            """newBase / os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue"""
            zipping.write(os.path.join(foldername,filename))
    zipping.close()
    print("Done")
zipfiles("F:\\testing\\JP Morgan Internship")