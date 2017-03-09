'''This file defines several base directors, which will be called
by other pipeline routines'''


def base_data():
    base = '/data/ksp/data/PROCESSED/'
    return base


def base_gdrive():
    base = '/data/ksp/gdrive/ksp.publish/moon/Night-by-Night/'
    return base


def base_foxtrot():
    '''Defines addition to path on Froxtrot to get to testfiles'''
    base = '/Users/mdrout/Research/KMTNet/kmtshi_testfiles'
    return base

def jpeg_path(gdrive_pdf):
    '''Defines path to a jpeg folder given string with the gdrive s.pdf
    Form = N2223-1.Q2.B.170120_0117.C.062448D724-223052D3.18D962.0D004.0000.pdf'''

    gdrive_txt = gdrive_pdf.split('.')
    gdrive_f = gdrive_pdf.split('.pdf')[0]

    fld = gdrive_txt[0].split('-')[0]
    sfld = gdrive_txt[0]
    quad = gdrive_txt[1]

    base = '/data/ksp/data/PROCESSED/'+fld+'/'+sfld+'/'+quad+'/B_filter/Subtraction/JPEG_TV_IMAGES/'+gdrive_f+'/'+gdrive_f

    return base