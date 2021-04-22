translations = {"Dragon curve": {"F": "F", "X": "X+YF+", "Y": "-FX-Y", "-": "-", "+": "+"},
                "Hilbert curve": {"+": "+", "-": "-", "F": "F", "A": "+BF-AFA-FB+", "B": "-AF+BFB+FA-"},
                "Koch snowflake": {"+": "+", "-": "-", "F": "F+F--F+F"},
                "Levi C curve": {"F": "+F--F+", "+": "+", "-": "-"},
                "Plant": {"+": "+", "-": "-", "[": "[", "]": "]", "X": "F-[[X]+X]+F[+FX]-X", "F": "FF"},
                "Pythagoras tree": {"1": "11", "0": "1[-0]+0"},
                "Sierpinski curve": {"F": "F", "G": "G", "+": "+", "-": "-", "X": "XF+G+XF--F--XF+G+X"},
                "Sierpinski curved triangle": {"F": "G-F-G", "G": "F+G+F", "+": "+", "-": "-"},
                "Sierpinski square curve": {"F": "F", "G": "G", "+": "+", "-": "-", "X": "XF-F+F-XF+F+XF-F+F-X"},
                "Sierpinski square": {"+": "+", "-": "-", "C": "CfCfC-f+C-f+C--f--C--f--C+f-C+f-", "f": "fff"},
                "Sierpinski triangle": {"F": "F-G+F+G-F", "G": "GG", "+": "+", "-": "-"},
                "Tree": {"1": "21", "0": "1[-20]+20"}}

start_position = {"Dragon curve": (270, 110), "Hilbert curve": (-330, -310), "Koch snowflake": (-300, 170),
                  "Levi C curve": (-250, 200), "Plant": (0, -340), "Pythagoras tree": (0, -340),
                  "Sierpinski curve": (0, 340), "Sierpinski curved triangle": (-400, -340),
                  "Sierpinski square curve": (0, -340), "Sierpinski square": (-335, -320),
                  "Sierpinski triangle": (-400, -340), "Tree": (0, -390)}

axioms = {"Dragon curve": "FX", "Hilbert curve": "A", "Koch snowflake": "F--F--F",
          "Levi C curve": "F", "Plant": "X", "Pythagoras tree": "0", "Sierpinski curve": "F--XF--F--XF",
          "Sierpinski curved triangle": "F-G-F", "Sierpinski square curve": "F+XF+F+XF",
          "Sierpinski square": "C", "Sierpinski triangle": "F-G-G", "Tree": "22220"}

angles = {"Dragon curve": 90, "Hilbert curve": 90, "Koch snowflake": 60,
          "Levi C curve": 45, "Plant": 25, "Pythagoras tree": 45, "Sierpinski curve": 45,
          "Sierpinski curved triangle": 60, "Sierpinski square curve": 90,
          "Sierpinski square": 90, "Sierpinski triangle": 120, "Tree": 16}


iterations = {"Dragon curve": 12, "Hilbert curve": 6, "Koch snowflake": 4,
              "Levi C curve": 13, "Plant": 7, "Pythagoras tree": 8, "Sierpinski curve": 5,
              "Sierpinski curved triangle": 8, "Sierpinski square curve": 5,
              "Sierpinski square": 4, "Sierpinski triangle": 7, "Tree": 12}

lengths = {"Dragon curve": 10, "Hilbert curve": 10, "Koch snowflake": 7,
           "Levi C curve": 5.5, "Plant": 2, "Pythagoras tree": 2.9, "Sierpinski curve": 6.3,
           "Sierpinski curved triangle": 3, "Sierpinski square curve": 5.5,
           "Sierpinski square": 8, "Sierpinski triangle": 6.2, "Tree": 11}

pensizes = {"Dragon curve": 3, "Hilbert curve": 3, "Koch snowflake": 2,
            "Levi C curve": 3, "Plant": 1, "Pythagoras tree": 2, "Sierpinski curve": 2,
            "Sierpinski curved triangle": 2, "Sierpinski square curve": 2,
            "Sierpinski square": 1, "Sierpinski triangle": 2, "Tree": 16}

shapes = ["Dragon curve", "Hilbert curve", "Koch snowflake",
          "Levi C curve", "Plant", "Pythagoras tree", "Sierpinski curve",
          "Sierpinski curved triangle", "Sierpinski square curve",
          "Sierpinski square", "Sierpinski triangle", "Tree"]

colors = ["Black", "White", "Red",
          "Orange", "Yellow", "Green",
          "Blue", "Dark blue", "Purple",
          "Brown", "Pink", "Gray"]
