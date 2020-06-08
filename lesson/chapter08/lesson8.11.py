import os
import pathlib
import glob
import shutil

# ファイルが有るか
print(os.path.exists('test.txt'))

# ファイルかどうか
print(os.path.isfile('test.txt'))

# ディレクトリか否か
print(os.path.isdir('../../design'))

# ファイルを変更
os.rename('test.txt', 'renamed.txt')

# # シムリンク(シンボリックリンク)
# os.symlink('renamed.txt', 'symlink.txt')

# ファイルがあったら不可
# os.mkdir('test_dir')

# os.rmdir('test_dir')

# # ファイルの作成
# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

# # ls
# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))
# # ['test_dir2']

# ファイル一覧を表示
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# print(glob.glob('test_dir/test_dir2/*'))

# shutil.copy('test_dir/test_dir2/empty.txt','test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))

# shutil.rmtree('test_dir')
# print(os.getcwd())