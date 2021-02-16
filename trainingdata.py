import textextractor as te
import re

image_to_text=te.img_to_str()


def find_text(image_to_text):  #finding the Starting and ending indexes of Entities
    image_to_text=image_to_text
    for i in image_to_text:
        print("The original string is : " + str(i))
        res = [(ele.start(), ele.end() - 1) for ele in re.finditer(r'\S+', i)]             
        print("Word Ranges are : " + str(res))
        
        
        
        
TRAIN_DATA = [
    (image_to_text[0], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[1], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[2], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[3], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[4], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[5], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[6], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[7], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[8], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[9], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[10], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[11], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[12], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[13], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[14], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[15], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[16], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[17], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[18], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[19], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[20], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[21], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[22], {
       'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[23], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[24], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[25], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[26], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[27], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[28], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[29], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[8], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[30], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[31], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[32], {
        'entities': [(64, 76, 'ACCHOLDER'),(79,90,'FATHER NAME'),(91,101,'DOB'),(130,140,'ACCNO')]
    }),
    (image_to_text[33], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[34], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[35], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[36], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[37], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[38], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[39], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[40], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[41], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[42], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[43], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[44], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[45], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[46], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[47], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[48], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[49], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[50], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[51], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[52], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[53], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[54], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[55], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[56], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[57], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[58], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[59], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[60], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[61], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[62], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[63], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[64], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[65], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[66], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[67], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[68], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[69], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[70], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[71], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[72], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[73], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[74], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[75], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[76], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[77], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[78], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[79], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[80], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[81], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[82], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[83], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[84], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[85], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[86], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[87], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[88], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[89], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[90], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[91], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[92], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[93], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[94], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[95], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[96], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[97], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[98], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[99], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[100], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[101], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[102], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[103], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[104], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[105], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[106], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[107], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[108], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[109], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[110], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[111], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[112], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[113], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[114], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[115], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[116], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[117], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[118], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[119], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[120], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[121], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[122], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[123], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[124], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[125], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[126], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[127], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[128], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[129], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[130], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[131], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[132], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[133], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[134], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[135], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[136], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[137], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[138], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[139], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[140], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[141], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[142], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[143], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[144], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[145], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[146], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[147], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[148], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[149], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[150], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[151], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[152], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[153], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[154], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[155], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[156], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[157], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[158], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[159], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[160], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[161], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[162], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[163], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[164], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[165], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[166], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[167], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[168], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[169], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[170], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[171], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[172], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[173], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[174], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[175], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[176], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[177], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[178], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[179], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[180], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[181], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[182], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[183], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[184], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[185], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[186], {
        'entities': [(64, 76, 'ACCHOLDER'),(79,90,'FATHER NAME'),(91,101,'DOB'),(130,140,'ACCNO')]
    }),
    (image_to_text[187], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[188], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[189], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[190], {
        'entities': [(64, 76, 'ACCHOLDER'),(79,90,'FATHER NAME'),(91,101,'DOB'),(130,140,'ACCNO')]
    }),
    (image_to_text[191], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[192], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[193], {
        'entities': [(68, 89, 'ACCHOLDER'),(106,120,'FATHER NAME'),(121,131,'DOB'),(159,169,'ACCNO')]
    }),
    (image_to_text[194], {
        'entities': [(37, 47, 'ACCHOLDER'),(75,93,'FATHER NAME'),(94,104,'DOB'),(131,141,'ACCNO')]
    }),
    (image_to_text[195], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[196], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[197], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[198], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    }),
    (image_to_text[199], {
        'entities': [(64, 76, 'ACCHOLDER'),(85,94,'FATHER NAME'),(99,109,'DOB'),(136,146,'ACCNO')]
    })]







