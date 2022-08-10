import zipfile
import os
import json
import pygame
import psutil

class Program:
    def __init__(self, filename, screen):
        self.filename = filename
        self.zip = zipfile.ZipFile(filename)
        self.screen = screen

    def run(self):

        # Append dependencies for future use.
        with open("../safeInfo.json") as f:
            safeInfo = json.load(f)
            for dependency in self.zip.open("lib.txt", mode="r").read().split("\n"):
                if not dependency in safeInfo["library"]:
                    safeInfo["library"].append(dependency)
                    os.system(f"pip install {dependency}")
        with open("../safeInfo.json", "w") as f:
            json.dump(safeInfo, f)

        # Loading the program
        loaded = {}
        with self.zip.open("loading.py").read() as f:
            exec(f.read(), {"loaded": loaded, "pygame": pygame, "surface": self.screen, "psutil": psutil})

        # Running the program
        with self.zip.open("__init__.py").read() as f:
            g_scope = globals().copy()
            g_scope["loaded"] = loaded
            l_scope = {}
            exec(f.read(), g_scope, l_scope)


if __name__ == "__main__":
    file = r"C:\Users\helli\PycharmProjects\PyOS\Drive\Admin\Desktop\test.prog"
    p = Program(file, None)
    p.run()
