#%%
from tmdw import counter, DictInv, getInput, file_reader, output

def counter_test():
    assert counter("this this this that this") == {'that': 1, 'this': 4,}, "Error in counter test"
    print("counter test done")

def DicInv_test():
    flag = True

    tmdwDict = DictInv({'apple': 10, 'ice' : 14, 'red': 5, 'tmdw': 100})
    testDict = {'tmdw': 100, 'ice': 14, 'apple': 10, 'red': 5}
    
    for (k,v), (kt,vt) in zip(tmdwDict.items(),testDict.items()):
        if k != kt:
            flag = False
            break
        if v != vt:
            flag = False
            break 

    assert flag == True , "Error in DictInv"
    print("DictInv test done")


def file_reader_test():
    testfile = "text_test.txt"
    # str = "this is first line this is decond line "
    # assert file_reader(file) == ""
    # f = open(file, "r")
    text = file_reader(testfile)
    assert text == 'this is first line\nthis is second line ', "Error in file_reader"
        


if __name__ == "__main__":

    counter_test()
    DicInv_test()
    file_reader_test()
    print("Everything passed")
    
    


