import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=[ ('2007', 'train'),  ('2007', 'test')]
classes = ['nvidia', 'huawei', 'huawei_text', 'cocacola', 'levis', 'milka', 'burgerking_text', 'mcdonalds', 'mercedesbenz', 'heineken_text', 'pepsi', 'pepsi_text', 'fly_emirates', 'dhl', 'aldi', 'nike', 'nike_text', 'rittersport', 'colgate', 'santander', 'santander_text', 'audi', 'becks', 'paulaner', 't-mobile', 'apple', 'starbucks', 'texaco', 'carlsberg', 'hyundai', 'wii', 'stellaartois', 'canon', 'supreme', 'subway', 'prada', 'adidas', 'guinness', 'obey', 'soundrop', 'allianz', 'allianz_text', 'fosters', 'cvspharmacy', 'intel', 'marlboro_text', 'hsbc', 'hsbc_text', 'esso', 'audi_text', 'michelin', 'head_text', 'amazon', 'ford', 'shell', 'shell_text', 'hp', 'chanel', 'wellsfargo_text', 'lacoste', 'chanel_text', 'adidas1', 'bellataylor', 'ferrari', 'nissan', 'singha', 'pampers', 'bem', 'alfaromeo', 'lv', 'ups', 'batman', 'volkswagen', 'volkswagen_text', 'bridgestone', 'bridgestone_text', 'target', 'target_text', 'williamhill', 'bmw', 'kia', 'rolex', 'kelloggs', 'redbull', 'redbull_text', 'caterpillar', 'uniqlo', 'uniqlo1', 'bosch', 'bosch_text', 'anz', 'corona', 'volvo', 'yonex', 'yonex_text', 'kraft', 'kitkat', 'gucci', 'marlboro', 'mk', 'visa', 'porsche', 'erdinger', 'lexus', 'hm', 'google', 'medibank', 'nbc', 'bionade', 'head', 'blizzardentertainment', 'heineken', 'toyota', 'nivea', 'costco', 'xbox', 'hermes', 'reebok', 'reebok_text', 'aspirin', 'bayer', 'citroen', 'citroen_text', 'total', 'pizzahut', 'pizzahut_hut', 'cvs', 'youtube', 'android', 'budweiser_text', 'lego', 'cartier', 'miraclewhip', 'philadelphia', 'velveeta', 'yamaha', 'coke', 'tsingtao', 'puma', 'puma_text', 'nb', 'infiniti', 'infiniti_text', 'zara', 'aral', 'armitron', 'bankofamerica', 'umbro', 'microsoft', 'apc', 'sprite', 'sega', 'wellsfargo', 'mitsubishi', 'hisense', 'vaio', 'optus', 'jurlique', 'chevrolet', 'chevrolet_text', 'chimay', 'optus_yes', 'mini', 'blackmores', 'olympics', 'base', 'fedex', 'facebook', 'amcrest', 'amcrest_text', 'budweiser', 'homedepot_text', 'lexus_text', 'danone', 'jacobscreek', 'jackinthebox', 'chickfila', 'bik', 'gap', 'unitednations', 'axa', 'carters', 'cpa_australia', 'aldi_text', 'tnt', 'rolex_text', 'recycling', 'ikea', 'mercedesbenz_text', 'renault', 'bbc', 'evernote', 'tacobell', 'basf', 'burgerking', 'mtv', 'comedycentral', 'unicef', 'apecase', 'loreal', 'nescafe', 'nissan_text', 'bfgoodrich', 'honda', 'honda_text', 'samsung', 'millerhighlife', 'cheetos', 'doritos', 'fritos', 'lays', 'ruffles', 'tostitos', 'hersheys', 'airness', 'corona_text', 'hyundai_text', 'maxxis', 'panasonic', 'barclays', 'gildan', 'adidas_text', 'gillette', 'venus', 'americanexpress_text', 'quick', 'hh', 'standard_liege', 'esso_text', 'windows', 'ec', 'motorola', 'firefox', 'dunkindonuts', 'oracle', 'benrus', 'cisco', 'jcrew', 'goodyear', 'siemens', 'underarmour', 'londonunderground', 'philips', 'nasa', 'schwinn', 'republican', 'generalelectric', 'suzuki', 'walmart_text', 'vodafone', 'tommyhilfiger', 'johnnywalker', 'ibm', 'northface', 'subaru', '3m', 'dexia', 'accenture', 'mcdonalds_text', 'carglass', 'lamborghini', 'walmart', 'citi', 'maserati', 'fritolay', 'rbc', 'netflix', 'mastercard', 'skechers', 'toyota_text', 'boeing', 'boeing_text', 'timberland', 'marlboro_fig', 'porsche_text', 'kodak', 'allett', 'bankofamerica_text', 'aluratek', 'aluratek_text', 'opel', 'bottegaveneta', 'select', 'twitter', 'mobil', 'disney', 'teslamotors', 'pepsi_text1', 'homedepot', 'playstation', 'hanes', 'calvinklein', 'internetexplorer', 'barbie', 'scion_text', 'yahoo', 'espn', 'aquapac_text', 'bacardi', 'anz_text', 'jagermeister', 'spar', 'spar_text', 'bbva', 'thomsonreuters', 'tissot', 'warnerbros', 'converse', 'heraldsun', 'asus', 'chiquita', 'athalon', 'bulgari', 'costa', 'us_president', 'poloralphlauren', 'superman', 'bershka', 'drpepper', 'lacoste_text', 'reeses', 'mccafe', 'verizon', 'verizon_text', 'luxottica', 'spiderman', 'kfc', 'armani', 'chevron', 'wordpress', 'sony', 'soundcloud', 'lg', 'nintendo', 'coach', 'at_and_t', 'firelli', 'airhawk', 'ebay', 'tigerwash', 'abus', 'sunchips', 'americanexpress', 'jello', 'maxwellhouse', 'planters', 'bellodigital', 'bellodigital_text', 'sap', 'shell_text1', 'reebok1', 'lotto']

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(year, image_id):
    in_file = open('VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id))
    out_file = open('VOCdevkit/VOC%s/labels/%s.txt'%(year, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for year, image_set in sets:
    if not os.path.exists('VOCdevkit/VOC%s/labels/'%(year)):
        os.makedirs('VOCdevkit/VOC%s/labels/'%(year))
    image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg\n'%(wd, year, image_id))
        convert_annotation(year, image_id)
    list_file.close()

