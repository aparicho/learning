from pathlib import Path
import os
print(Path.cwd())
os.chdir('C:\\Windows\\System32')
print(Path.cwd())
os.makedirs('C:\\delicious\\walnut\\waffles')
Path(r'C:\Users\Al\spam').mkdir()
Path.cwd() / Path('my/relative/path')
os.path.abspath('.')
os.path.abspath('.\\Scripts')
os.path.isabs('.')
os.path.isabs(os.path.abspath('.'))
p = Path('C:/Users/Al/spam.txt')
p.anchor
p.parent # This is a Path object, not a string.
p.name
p.stem
p.suffix
p.drive
Path.cwd().parents[0]
#WindowsPath('C:/Users/Al/AppData/Local/Programs/Python')
Path.cwd().parents[1]
#WindowsPath('C:/Users/Al/AppData/Local/Programs')
Path.cwd().parents[2]
#WindowsPath('C:/Users/Al/AppData/Local')
Path.cwd().parents[3]
#WindowsPath('C:/Users/Al/AppData')
Path.cwd().parents[4]
#WindowsPath('C:/Users/Al')
Path.cwd().parents[5]
#WindowsPath('C:/Users')
Path.cwd().parents[6]
#WindowsPath('C:/')

p = Path('C:/Users/Al/Desktop')
list(p.glob('*.txt'))
list(p.glob('project?.docx'))

winDir = Path('C:/Windows')
notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
calcFile = Path('C:/Windows/System32/calc.exe')
winDir.exists()
#True
winDir.is_dir()
#True
notExistsDir.exists()
#False
calcFile.is_file()
#True