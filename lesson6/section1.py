
import os, shutil

def fillInGaps(folder, prefix):
	folder = os.path.abspath(folder)
	indexList = []
	extension = None
	numberLen = None
	for entry in os.listdir(folder):
		if os.path.isdir(entry) or not entry.startswith(prefix):
			continue
		name, ext = os.path.splitext(entry)
		currentIndex = int(name[len(prefix):])
		if extension is None:
			extension = ext
		if numberLen is None:
			numberLen = len(name[len(prefix):])
		indexList.append(currentIndex)

	indexList.sort()
	largestIndex = indexList[-1]
	if largestIndex == len(indexList):
		print('No gap in all files with the given prefix (', prefix, ')', sep = '')
		return

	index = 1
	for i in range(0, len(indexList)):
		if index == indexList[i]:
			index += 1
			continue
		oldFile = folder + os.path.sep + prefix + '0'*(numberLen-len(str(indexList[i]))) + str(indexList[i]) + extension
		newFile = folder + os.path.sep + prefix + '0'*(numberLen-len(str(index))) + str(index) + extension
		print('Filling the gap by moving', oldFile, 'to', newFile)
		shutil.move(oldFile, newFile)
		index += 1

folder = 'folder'
prefix = 'spam'
fillInGaps(folder, prefix)