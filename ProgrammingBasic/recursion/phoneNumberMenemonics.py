
def phoneNumberMnemonics(phoneNumber):
  currentMenomics = [''] * len(phoneNumber)
  menomicsResult = []
  helper(0,currentMenomics, phoneNumber,menomicsResult)
  
  return menomicsResult

def helper(idx, currentMenomics, phoneNumber, menomicsResult):
  if idx == len(phoneNumber):
    menomicsResult.append(''.join(currentMenomics))
  else:
    currentDigit = phoneNumber[idx]
    letters = mnemonics[currentDigit]
    for letter in letters:
        currentMenomics[idx] = letter
        helper(idx+1, currentMenomics, phoneNumber, menomicsResult)
        




mnemonics = {
'0': ['0'],
'1': ['1'],
'2': ['a','b','c'],
'3': ['d','e','f'],
'4': ['g','h','i'],
'5': ['j','k','l'],
'6': ['m','n','o'],
'7': ['p','q','r','s'],
'8': ['t','u','v'],
'9': ['w','x','y', 'z']

}

