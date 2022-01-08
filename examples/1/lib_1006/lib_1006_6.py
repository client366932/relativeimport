import relativeimport

lib_998_1 = relativeimport(__file__, "../lib_998/lib_998_1")
lib_998_2 = relativeimport(__file__, "../lib_998/lib_998_2.py")
lib_998_3 = relativeimport(__file__, "../lib_998/lib_998_3")
lib_999_1_1 = relativeimport(__file__, "../lib_999/lib_999_1/lib_999_1_1")
lib_999_2_5 = relativeimport(__file__, "../lib_999/lib_999_2/lib_999_2_5.py")
lib_999_3_7 = relativeimport(__file__, "../lib_999/lib_999_3/lib_999_3_7")
lib_1000 = relativeimport(__file__, "../lib_1000")
lib_1002 = relativeimport(__file__, "../lib_1002.py")
lib_1003 = relativeimport(__file__, "../lib_1003")

if __name__ == "__main__":
    for im in [
        lib_998_1, lib_998_2, lib_998_3, lib_999_1_1,
        lib_999_2_5, lib_999_3_7, lib_1000,
        lib_1002, lib_1003
        ]:
        print('v in %s is %s' % (im.__name__, im.v))
