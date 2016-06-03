input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

alph = list("abcdefghijklmnopqrstuvwxyz")
shifted = list()

for i in alph:
    shifted.append(chr((ord(i) - 97 + 2)%(26) + 97))

convf = dict(zip(alph, shifted))

def translate(input, conversion_dict):
    output = ""

    for i in input:
        try:
            output += convf[i]
        except KeyError:
            output += i

    return output

print translate(input, convf)
print translate("map", convf)
