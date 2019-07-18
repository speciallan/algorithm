#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        arr = []
        # print(words)

        # 'a', ''
        if '' in words:

            # [1,2]
            blank = []
            for i in range(len(words)):
                if words[i] == '':
                    blank.append(i)

            for i in range(len(words)):
                if self.isHuiwencuan(words[i]):
                    for j in range(len(blank)):
                        if i != blank[j] and [i,blank[j]] not in arr:
                            arr.append([i,blank[j]])
                        if i != blank[j] and [blank[j], i] not in arr:
                            arr.append([blank[j], i])

        # 聚类统计
        map = {}
        for i in range(26):
            map[chr(i + ord('a'))] = []

        for i in range(len(words)):
            for j in range(len(words[i])):
                map[words[i][j]].append(i)

        for i in range(len(words)):

            if words[i] == '':
                continue

            # 翻转
            # reverse = words[i][::-1]
            # if reverse in words:
            #     index = words.index(reverse)
            #     if index != i:
            #         arr.append([i,index])
            #         arr.append([index,i])

            # 把字母加起来 abcd 的词序号
            cur_arr = []
            for j in range(len(words[i])):
                alpha = words[i][j]
                cur_arr.extend(map[alpha])

            # 去重
            cur_arr1 = []
            for element in cur_arr:
                if element not in cur_arr1:
                    cur_arr1.append(element)

            for j in cur_arr1:
                a = words[i] + words[j]
                b = words[j] + words[i]

                if i != j and self.isHuiwencuan(a):
                    # print(a,i,j)
                    arr.append([i,j])

                if i != j and self.isHuiwencuan(b):
                    # print(b,j,i)
                    arr.append([j,i])

        # 去重
        new_arr = []
        for i in range(len(arr)):
            if arr[i] not in new_arr:
                new_arr.append(arr[i])

        return new_arr

    def isHuiwencuan(self, s):

        if len(s) == 0:
            return False

        if len(s) == 1:
            return True

        if len(s) == 2 and s[0] == s[1]:
            return True

        i,j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True


if __name__ == "__main__":

    # words = ["abcd","dcba","lls","s","sssll"]
    # words = ["bat","tab","cat"]
    words = ["jbbfchhghiidiabc","fggahdbgg","hdbcdcgahhabe","jfce","cfd","bfcdddhc","ifcbcjfhgdjijgii","jafaiadefcidibeffhg","jceei","ifadccfdjade","cbhbh","eadeadjeebeg","cafjeebdhbj","echbhggjefc","jjcgaecbgjagabhfceff","fede","gcg","fcgiifbjjijidgdcagff","behcfh","ghb","gjahgdggcfd","bgbccbedfggbaecjic","iegccagjef","jicibihjajaajid","agiafdbbbbhe","bciadec","ijifhhdgdd","agaijigieicdga","adaieajh","i","eeihecdhdcccjd","bjediigfegfadbedg","bjjbgfiggcjjiebi","icdjb","hbhgfbdibeii","bjjdgfij","heijjhheifeedg","cajg","dce","cccihgfaf","gfbcafihfjefe","abgjeechdfgdegfdg","agcejhiaacci","di","cjbbaejdifehecb","giih","bg","hhhjjdgif","efdcdeaifcjg","dj","jag","fchhfbgfeejdgbc","hccjhdadhfbacahebad","ajedbeafbcbchbeci","ch","aiiajiibcbeahc","ggfggbcjdd","eedihaffdeij","fcfi","cfbd","ccifiidjifcge","dffjdjidehh","ccejcahhd","eaeehbchiefhie","ifjihg","jjddgfhdeebcd","aefbhecjgjg","caeedcdbgddbhjfahcj","aafg","dgifaieaejaehgcacfi","ggicjeheijdb","aaifcaeaebfhb","ifdebbfbcjjf","jbddih","ajhgbbcebaca","djjigjeahihijeabfgg","gjahdeffdece","c","ejgcgacacefgjdcj","efdebbebia","hbeiaabjigbghggchhg","fehe","gihhgcbijgbiicegiif","hbiedddeihfadag","fecbbcfaiggfd","h","cabdbh","eceabcdbchehdhfjbj","ejai","cjfeahcjd","ejcibibcaj","jibejjdfdejfhcfheb","dfgdgibcaeahjdg","haihbdacfajbbbggfii","fcbbhaecfeii","cafcfdbheeghh","fiighfh","fbddheedbadhihfccba","cacddagabaahjh","eejjgbjiffgc","ecgbdcdcedaeijbg","fejiiebghbidch","fia","fjjdgicbgdjaf","gb","aeeafiajfaiahgbhegf","jfhejdfjjhaji","ggacbhheaiegabafdee","jdfjch","ejcgg","gedhch","dibja","idiaeebbdecjfdejibf","hibhi","hjfejdggb","g","jfbjgdih","djabbgdfcjjffgd","dabdij","dajcfdjeh","ehjaice","iihjeejhbdjh","did","eiidghaf","gfaceddh","dadhjgeihjdgbaeie","fef","hjfffeiddibfge","hhjgiegbigbfcjc","cijg","f","fjdacbgihejcifgfj","ffg","bbhcggiheifcihegdd","ecifejhg","edhjebfhbcacgggehead","dbcffhigcg","cjeeccgdcgaj","cdjichajjjadedb","cbfgfjefafgdfjeb","cgjgf","hjibcjfjgff","cagffj","eaaejde","ibfadagfaddjdcdfdca","hcjibdaj","eehbh","aifbdgbabaffbgaajh","bddcaigfbgae","bhfibjjgcabjef","eeh","ghbibfgghajbfaia","bjdbfigfiecibad","daehaebeigjgcaag","gcfeec","ajagigibhb","jcfhdbfhbidihjf","ehiej","b","chcbcacijcbdigh","jjibbai","ajefcdfccehc","aijhdhhffgh","hcecaaae","dieejdjjhaffdbebaij","gid","ieddfhbcjgidjichd","cd","fec","iicjhgad","ege","ajaa","cbhcfih","dfaahaecibea","fdbchcg","ahaagbffeeicdhed","gbdjjiigjgh","gc","ahggef","afcagacdaf","hefbfbc","egfgdhfgh","dbibcd","higjjcfaiajfchdcjgf","hgbgigciii","ajac","bi","bdbeefdccbfcijheaae","hecegijfbcbfegaj","heb","fggaaddbfaeihgde","eidgda","hibccahhfhjeehdfg","fjac","gebadedccdeij","ebieajiddfbgac","jfcgigejcjfaaefcbd","fbjfjggghcjigcbjh","cbebhb","cgfjhijfeebcehga","d","fafdbhcgij","hfecibjde","jabjiagceiffja","cigciagcae","iiggaddcbdjgeeec","afjhecbfc","gcadchgjcgjcbf","aejdjadeghebjbhef","iegggajjadgf","iffchijiig","fehac","ibiidchfhhjgja","hdiefegeaidggc","abgghhfdhigidjhcg","bhdjfghjegb","edgjecehcbecfaigebd","ggciaibejefjjchehb","gefdjffbbccgdcd","ddjhdfhe","jiehgjighh","hajdab","bfbhaiaiihdaeicdbaji","gebecj","igjhfdaccjfajf","ghhgbedhj","dghjhi","ijcbdacjji","fcadd","ajedgieagf","cggjabejfhagej","afhddgadfdef","fdhifhhe","hhibdjhbjiah","gdj","cfjd","cja","igfacfhdc","ahhcj","dhjafgdhcebgbefc","bdcaebdbbdijhbi","gji","decibf","dghabac","jfd","idhjbcabfgfgdg","ibgehghhfeabi","eegggihcgj","ffaibcgae","fhcegf","aecghib","iajeiifdfibaeg","cfabfdjebbffcaaf","gdihgdijdgfhfgajfh","febjaad","aedaaifgied","bcjeahcgbjif","cic","fjjgebbbbhjfch","hedahdfeehdeccgecg","fcdgjfiegd","dcejgjehhh","dgdchghcdhigcai","hhbijie","cfi","aagchcie","jiagie","jfhfajeec","faidbed","effjdajccbcfhadd","aababdaedhijdchbic","feeggjfgbe","fbaecbaaeagiiieadcbd","iijfgf","bfaaideabfachicf","gbdhcdecjchfd","edejfg","dfjhdjiiafccafjdcdi","ici","gajeegbfifg","fadjjcgjaigfgi","jcfhdigj","jghcf","hjbejcdjbiacjjca","cadjhce","fj","aahbeagbgbi","ea","e","jihghibjhdcbcbhchia","eegi","febgja","digj","iabfieafbgeahfbd","eideachhbffdjbbaj","aeibcicfcjihjdabcfej","eidhieajdjbjgcefg","fifhfjffccdffcfc","jcgdhbgdebhbhhi","jfbjfdcfb","jdicicdcf","hfbbcebhhjiehacedd","ehffbjcgdhfg","dhhciggaiafdi","ggia","aihdbi","baeebcieai","cccg","j","ffjhagjgjhaggh","gchcbeifecjfiaf","diehajgcdddafhigdb","djdfdadjhjfdeee","edbidaadegficja","jhbefhbbgicgajjfc","gdahbbhce","fgfaeajgj","cgghbejcheg","bcfbijcja","adchijheebjc","iaii","aeeaheiegfbg","aiij","bhffecejfgif","gjf","bgeddgg","iigbdgihcdbgiaaa","fdbhfbeeifjgif","giacjagcfffefgddbdf","jcdacggdfa","gebahgddgfjecigdahag","ccjihh","gchecfbfbeaahfei","igiceaee","ajd","baifc","giiejbdcecbcfiiiccji","fh","fibaaedhhighcjejgah","iidaiachadde","gefadgeagjjfacdhgc","ahdabhcbigeffbihffh","fiiffceeafabhh","ceicdac","fijfibadfajfbbacajej","gjeaheeefgecifg","dejbbddcfiaiee","ahidf","gbddjeaebfcbh","ajdbcfjhdijcedhfg","eiiddjhdhdab","dijgid","eh","iebgijhhffecddih","dfiad","aaa","bead","cdhbdcjcgbhgc","cih","acbgjehd","hb","fdjdficca","bafbchhd","jhjg","gbcjfjcbgddg","heg","gigcb","bhgjigdbhfbfaa","jjch","fgcccc","bhihbbbifeiiabdh","bifbbcfgbdie","dfeaaiebidaici","cieafehafgh","bicagfici","ibj","dgdcge","chfadg","gaaadccfgadi","hjdbcaafa","gfdc","bgfecijcjiicdjicdi","idgdeejdeidhiecfaf","cdbbdeigjfihig","ifdf","aiebdcbfaegbeea","jahggbbeejgcebab","bcgajcceggfiejj","agaffg","fbgbaijihddjjfh","fgibffbf","bf","cdcahbeadhffeedaej","ijeidheehcbacf","igji","ehhadgjaajf","hejdjaajeedgfcgbhcj","fcecjjhjc","jjieaiehjecd","cfifdbehdfbbafgajej","bd","jejfab","egdigaf","fggjechggfeagccff","bbijbediejhidfhc","iacjddbfdc","eeeddgabheiaj","aegcchdjhghb","hceahacijfddbfdfggie","idcgjceg","ggihecbgefgajj","jhcfcfcjbhbadgfifacc","fcffcje","idji","fggfjjifcff","jjghbgfgjeecdfi","eaaahbjiijccffiehb","adbac","cecjabddcdcgfdjcbj","jdbhiecbbdidihiba","ibaibdebhdfic","ab","igegbecd","bdedjfihdaeaheid","bhdidfbeccdhajia","eifjdeebdhchjedfc","gihfjf","ibahjcfagdgci","fhhijfcg","facdgacfieciai","eaiedbcgfegebei","cgcabhjjfebcf","bhiibhjdihbbdcd","jjfgejcheiddecbfafbi","ecjfjbbcf","eeafcjjjghfbbjgdghe","ef","fagidbi","dbbcahdfaf","bbichhhcihebceg","dcbagihdeh","edfcajcccge","igdeg","hg","hej","jihehhge","jhdfihbicfeei","fejihaggjjigaggcige","ddghfdd","dcbdji","ecbih","bbbihaieccdicggfihec","jciihdiiieiff","ajchbgfbfbejhi","hebi","biebciddfgabfg","fgibbjhja","eajchedegjhehjhbgchf","cjhggddj","ghjdfjhfcfibedbc","efcidfe","jb","gabihjggbabgbci","gjbidabfaij","cbbjccbejfejcabcg","ehgdihce","ggffgja","efhbffeeheaigigbcha","ceg","bhgbdjfedfhegfihajh","cafhicjbiidffich","febgbhiciad","gbcgbhhajagiejddf","hacafcefbhgjgji","dgh","djbghacaggg","bdafhieja","gjabdbdaigfadcjidg","djgajchgf","afeiddb","bb","hjdaaceifbj","jcaggicfdjidiefbgh","fc","ifhfefdhb","fjgbejfa","ga","cifjahchd","fbihejj","ccdgbifefjadidfehfia","beadcbfiagahj","jjghiggbhdadebfadch","ccihdgbhjbghdeahd","daabaediji","hifaihdgaji","efecjebebbcdehgbfacd","cfadghfhdj","gdigjcj","acdgbbcfhh","cbed","cj","hjjfbahhaeddidifia","cchagb","gaajiiajiffa","igaggehb","jccdcf","dedig","gjcjhhjhigigddfchfa","fgaiihebhfaacgbbihia","jahiejdadeda"]
    # words = ["a",""]

    solution = Solution()
    result = solution.palindromePairs(words)
    print(result)
