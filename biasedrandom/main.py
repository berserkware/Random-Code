import random

class biasedrandom():
    def brandrangenum(start: int, stop: int, biasednumbers: list, biaschance: int):
        if biaschance > 100:
            raise ValueError('biaschance cannot be bigger that 100.')

        for i in biasednumbers:
            if int(i) > stop or int(i) < start:
                raise ValueError('All biasednumber must be under stop and over start')
            elif isinstance(i, str) != False:
                raise ValueError('Your biasednumbers have to be ints')

        randomNumber  = random.randrange(start, stop)
        if random.uniform(0, 100) < biaschance:
            n = random.randrange(0, len(biasednumbers))
            return biasednumbers[n]
        else:
            return randomNumber

    def dbrandrangemol(start: int, stop: int, biasmorethan: int, biaslessthan: int, biaschance: int):
        if biaschance > 100:
            raise ValueError('biaschance cannot be bigger that 100.')

        if biasmorethan < start or biasmorethan > stop:
            raise ValueError('biasmorethan has to be has to be more than start and less than stop and less than biaslessthan')
        elif biaslessthan < start or biaslessthan > stop:
            raise ValueError('biaslessthan has to be has to be more than start and less than stop and more than biasmorethan')

        randomNumber  = random.randrange(start, stop)
        if random.uniform(0, 100) < biaschance:
            return random.randrange(biasmorethan, biaslessthan)
        else:
            return randomNumber

    def brandintnum(start: int, stop: int, biasednumbers: list, biaschance: int):
        return brandrangenum(start, stop+1, biasednumbers, biaschance)
    
    def brandintmol(start: int, stop: int, morethan: int, lessthan: int, biaschance: int):
        return brandintmol(start, stop+1, morethan, lessthan, biaschance)

    def bchoice(choices: list, biasedchoices: list, biaschance: int):
        if biaschance > 100:
            raise ValueError('biaschance cannot be bigger that 100.')

        result =  all(elem in choices  for elem in biasedchoices)
        if result:
            pass 
        else:
            raise IndexError('Your biased choices have to be in your choices')


        choice = random.choice(choices)
        if random.uniform(0, 100) < biaschance:
            return biasedchoices[random.randrange(0, len(biasedchoices))]
        else:
            return choice

    def bsample(sequence: list, size: int, biasedchoices: list, biaschance: int):
        if biaschance > 100:
            raise ValueError('chance cannot be bigger that 100.')

        if size > (len(sequence) - 1):
            raise ValueError('size cannot be bigger than the length of sequence')

        if size < 1:
            raise ValueError('size cannot be smaller than zero')

        result =  all(elem in sequence  for elem in biasedchoices)
        if result:
            pass 
        else:
            raise IndexError('Your biased choices have to be in your choices')

        sample = []

        while True:
            randomNum = random.randrange(0, len(sequence))
            randomPercent = random.uniform(0, 100)
            if randomPercent < biaschance:
                randomBias = random.randrange(0, len(biasedchoices))
                if biasedchoices[randomBias] not in sample:
                    sample.append(biasedchoices[randomBias])
                else:
                    randomChoice = sequence[random.randrange(0, len(sequence))]
                    if randomChoice not in sample:
                        sample.append(randomChoice)
            else:
                randomChoice = sequence[random.randrange(0, len(sequence))]
                if randomChoice not in sample:
                    sample.append(randomChoice)

            if len(sample) == size:
                break


        return sample
        
    def brandom(biasednumbers: list, biaschance: int):
        if biaschance > 100:
            raise ValueError('biaschance cannot be bigger that 100.')

        for i in biasednumbers:
            if int(i) > 1 or int(i) < 0:
                raise ValueError('All biasednumber must be under 1 and over 0')

        randomNumber  = random.random()
        if random.uniform(0, 100) < biaschance:
            n = random.randrange(0, len(biasednumbers))
            return biasednumbers[n]
        else:
            return randomNumber

    def buniform(start: int, stop: int, biasednumbers: list, biaschance: int):
        if biaschance > 100:
            raise ValueError('biaschance cannot be bigger that 100.')

        for i in biasednumbers:
            if int(i) > stop or int(i) < start:
                raise ValueError('All biasednumber must be under stop and over start')
            elif isinstance(i, str) != False:
                raise ValueError('Your biasednumbers have to be numbers')

        randomNumber  = random.uniform(start, stop)
        if random.uniform(0, 100) < biaschance:
            n = random.randrange(0, len(biasednumbers))
            return biasednumbers[n]
        else:
            return randomNumber

