def main():
    #Invert function present on the think python book
    def invert_dict(d):
        inverse = dict()
        for key in d:
                val = d[key]
                if val not in inverse:
                    inverse[val] = [key]
                else:
                    inverse[val].append(key)
        return inverse
    #Function using the setdefault built-in function from the dicionary class
    def enhanced_inverse_dict(normal_dict):
        invert_dict={}
        for key in normal_dict:
            invert_dict.setdefault(normal_dict[key],[]).append(key)
            #invert_dict.setdefault(normal_dict[key],[key].append(invert_dict.setdefault(normal_dict[key],[key])))
        return invert_dict
    test_dict={"pena":4,"tutor":5,"mais":4,"lupa":4,"teste":5,"alo":3}
    print(invert_dict(test_dict))
    print("-----------------------------".center(100))
    print(enhanced_inverse_dict(test_dict))


if __name__=='__main__':
    main()