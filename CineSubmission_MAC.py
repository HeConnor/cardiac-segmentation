#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 21:04
# @USER    : Connor
# @File    : CineSubmission_MAC.py
# @Software: PyCharm
# @Version  : Python-3.6
# @TASK:
import logging
import scipy.io as sio
import matplotlib.pyplot as plt
import os,glob,re
import numpy as np

def load_CineImages(patientdir):
    glob_search = os.path.join(patientdir, '*_sBTFE_BH_7_*.mat')
    matfiles = glob.glob(glob_search)
    if len(matfiles) == 0:
        logger.error("Couldn't find Cine-Short MAT file in {}. "
                     "Wrong directory?".format(patientdir))
        return
    for file in matfiles:
        data = sio.loadmat(file)
        images = data['I']
        images = images[0, 0]
        images = np.array(images[0])

    return images

def main():
    directory='E:\\717-3Lab\\MRI\\MAC'
    glob_search = os.path.join(directory,'Group*')
    subdir = glob.glob(glob_search)
    if len(subdir)==0:
        logger.error("Couldn't find Group listing file in {}. "
                            "Wrong directory?".format(directory))
        return
    # import operator
    # # 条件为真，返回前面内容
    # func = lambda x: [y for l in x for y in func(l)] if type(x) is list else [x]
    # patients0 =func([[os.path.join(pdir,p) for p in os.listdir(pdir)] for pdir in subdir])
    patients = [os.path.join(pdir, p) for pdir in subdir for p in os.listdir(pdir)]
    # operator.eq(patients,patients0)
    logger.info('Loading patient images ... ')
    for patient in patients:
        pass
        # images=load_CineImages(patient)

        # # display
        # plt.figure(figsize=(10, 5))
        # for index in range(3):
        #     plt.subplot(1, 3, index+1)
        #     plt.axis("off")
        #     plt.imshow(images[:,:,index], cmap=plt.cm.gray)
        # plt.show()


    logger.info('done!')


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)  # Log等级总开关
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.info('Build Cine Data Set ...')
    main()