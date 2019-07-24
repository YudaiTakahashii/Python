#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:29:55 2019

@author: takahashiyuudai
"""

#選択コピー
#フォルダ内の特定の拡張子を探して，新たなフォルダにまとめてコピーするプログラム
import re, os, shutil

#------------------------------------------------------------------------------
#pdf, jpg, doc(docx), xlsxの正規表現を作る
pdf_pattern = re.compile(r"""
^(.*?)    #ファイル名
(.pdf)$  #拡張子名
""", re.VERBOSE)

jpg_pattern = re.compile(r"""
^(.*?)    #ファイル名
(.jpg)$  #拡張子名
""", re.VERBOSE)

word_pattern = re.compile(r"""
^(.*?)    #ファイル名
((.doc)|(.docx))$  #拡張子名
""", re.VERBOSE)

excel_pattern = re.compile(r"""
^(.*?)    #ファイル名
(.xlsx)$  #拡張子名
""", re.VERBOSE)

Markdown_pattern = re.compile(r"""
^(.*?)    #ファイル名
(.md)$  #拡張子名
""", re.VERBOSE)

Python_pattern = re.compile(r"""
^(takayu_)
(.*?)    #ファイル名
((.py)|(.ipynb))$  #拡張子名
""", re.VERBOSE)

report_pattern = re.compile(r"""
^(17T0806M) 
""", re.VERBOSE)


#------------------------------------------------------------------------------
#正規表現を引数とした関数を作る
def FILE_organize(pattern, path, dir_name):
    print('FILE_orgnize...')
    print('-----------------------------------------------')
    os.chdir(path)    #指定されたpathに飛ぶ
    #適当なディレクトリを作成する
    number = 1
    while True:
        dir_file = dir_name + '_' + str(number)
        if not os.path.exists(dir_file):
            break
        number += 1
    os.mkdir(dir_file)    
    for foldername, subfolder, filenames in os.walk(path):
        for filename in filenames:
            mo = pattern.search(filename)
            if not mo == None:
                abs_path = os.path.join(os.path.abspath(foldername), filename)
                if dir_name in abs_path:
                    continue
                shutil.copy(abs_path, dir_file)
                print(abs_path)
    print('--------------------------------------------------------------------')
    print('FILE have been orgnaized')
                
                
#------------------------------------------------------------------------------               
print('指定されたファイルについて，拡張子が同じものを整理します')
path = input('カレントディレクトリからの相対パスか，絶対パスを入力してください : ')

if not os.path.isabs(path):
    path = os.path.abspath(path)
                
print('整理したい拡張子を以下から選んでください')
pattern = input('(1)PDF   (2)Excel  (3)Word  (4)jpg  (5)md  (6)Python:')

pat_num = int(pattern)

if pat_num == 1:
    FILE_organize(pdf_pattern, path, 'PDF')
elif pat_num == 2:
    FILE_organize(excel_pattern, path, 'Excel')
elif pat_num == 3:
    FILE_organize(word_pattern, path, 'Word')
elif pat_num == 4:
    FILE_organize(jpg_pattern, path, 'JPG')
elif pat_num == 5:
    FILE_organize(Markdown_pattern, path, 'Markdown')
elif pat_num == 6:
    FILE_organize(Python_pattern, path, 'Python')

else:
    print('適切な数字が入力されませんでした')


print('プログラムを終了します')                
                
