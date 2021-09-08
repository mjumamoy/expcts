# Export to Clean Transcript Script by Matthew Jumamoy
# mjumamoy@stanford.edu
# 9/7/21
# Usage: cts_vtt.py -flag input.vtt output.txt subjectname pseudonym
# A minimum of 3 arguments are required to run the script. Subjectname and Pseudonym are optional.
# Valid number of arguments: 3 or 5
# Valid Flags: -c, -ctab, -ctabanon, -canon
# Sources: https://stackoverflow.com/questions/25023233/how-to-save-python-screen-output-to-a-text-file, https://matplotlib.org/stable/users/installing.html, https://www.geeksforgeeks.org/reading-writing-text-files-python/, https://www.geeksforgeeks.org/python-string-replace/, https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file, and other Stackoverflow Posts
# Stanford Sources: https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1216/index.html, Class Resources from Fall 2019, https://cs.stanford.edu/people/nick/py/python-file.html

# py pip install webvtt-py before hand for dependency
import sys
import webvtt

# Universal Variables
args = sys.argv[1:]
filename = args[1]
output = open(args[2], "w")
output_plain = args[2]

# importing only caption text
def main():
    print('### Export to Clean Transcript v1.0 ###')
    print('Written by Matthew Jumamoy | github.com/mjumamoy | Sept. 7, 2021 | For assistance: mjumamoy@stanford.edu')
    print('  Required Dependencies: webvtt')
    print('  This script requires 3 or 5 arguments. No other amount of arguments are accepted.')
    print('  Valid Flags: -c, -ctab, -ctabanon, -canon')
    print('  Format: expcts.py [input.vtt] [output.vtt] [Interviewee Name] [Pseudonym]')
    print('  -> If you have a subject with a name used in the transcript that uses a space, make sure to use "" around their name. For example, if they used John Doe on Zoom. Use "John Doe" as the fourth argument.')
    print('  -> Make sure your VTT files are in the same directory as this .py file.')
    if len(args) == 3 and args[0] == '-c':
        grabcaption()
    if len(args) == 3 and args[0] == '-ctab':
        grabcaption()
        tab()
        end()
    if len(args) == 5 and args[0] == '-canon':
        grabcaption()
        pseudonym()
    if len(args) == 5 and args[0] == '-ctabanon':
        grabcaption()
        tab()
        pseudonym()

# Grabbing Captions and Creating New Lines for New Text Strings
def grabcaption():
    for caption in webvtt.read(filename):
        output.write(caption.text)
        output.write("\n")
    end()

# Replacing ": " with Tab character
def tab():
    with open(output_plain, "r") as file:
        output_tab = file.read()
    output_tab = output_tab.replace(': ', '\t')
    with open(output_plain, "w") as file:
        file.write(output_tab)

# Using Pseudonyms for Interviewees
def pseudonym():
    with open(output_plain, "r") as file:
        output_tab = file.read()
    subjectname = args[3]
    pseudonymname = args[4]
    output_anon = output_tab.replace(subjectname, pseudonymname)
    with open(output_plain, "w") as file:
        file.write(output_anon)

# Closing Output File
def end():
    output.close()

# Python Starting Arguments for main()
if __name__ == '__main__':
    main()