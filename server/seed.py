#!/usr/bin/env python3

# local imports
from app import app
from models import db, Image

def seed_data():

    # print("Deleting all previous data...")
    try:
        Image.query.delete()
        print("Existing data deleted.")
    except Exception as e:
        print(f"Error deleting data: {e}")

# seed vertical images 
    print("adding Images...")
    image_list =[]

    image1 = Image(
        title = "SLO",
        location = "San Luis Obispo, CA, USA",
        year = 2012,
        gallery = "Space",
        horizontal = False,
        path = "/images/20120428_SLO_076.jpg",
    )
    image_list.append(image1)

    image2 = Image(
        title = "Lille 26",
        location = "Lille, France",
        year = 2013,
        gallery = "Place",
        horizontal = False,
        path = "/images/20130418_Lille_026c.jpg",
    )
    image_list.append(image2)

    image3 = Image(
        title = "Lille 42",
        location = "Lille, France",
        year = 2013,
        gallery = "Place",
        horizontal = False,
        path = "/images/20130418_Lille_042.jpg",
    )
    image_list.append(image3)

    image4 = Image(
        title = "Istanbul 003",
        location = "Istanbul, Türkiye",
        year = 2013,
        gallery = "From-the-Hip",
        horizontal = False,
        path = "/images/20130419_Istanbul_003.jpg",
    )
    image_list.append(image4)

    image5 = Image(
        title = "Istanbul 070",
        location = "Istanbul, Türkiye",
        year = 2013,
        gallery = "Place",
        horizontal = False,
        path = "/images/20130419_Istanbul_070.jpg",
    )
    image_list.append(image5)

    image6 = Image(
        title = "Istanbul 038",
        location = "Istanbul, Türkiye",
        year = 2013,
        gallery = "Place",
        horizontal = False,
        path = "/images/20130420_Istanbul_038.jpg",
    )
    image_list.append(image6)

    image7 = Image(
        title = "Istanbul 117",
        location = "Istanbul, Türkiye",
        year = 2013,
        gallery = "From-the-Hip",
        horizontal = False,
        path = "/images/20130420_Istanbul_117_nc.jpg",
    )
    image_list.append(image7)

    image8 = Image(
        title = "IAD 003",
        location = "Dulles, VA, USA",
        year = 2013,
        gallery = "Airport",
        horizontal = False,
        path = "/images/20131019_IAD_003.jpg",
    )
    image_list.append(image8)

    image9 = Image(
        title = "Dune du Pilat 682",
        location = "Dune du Pilat, France",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/20140920_Dune_du_Pilat_682.jpg",
    )
    image_list.append(image9)

    image10 = Image(
        title = "Agra 141",
        location = "Agra, Uttar Pradesh, India",
        year = 2010,
        gallery = "Place",
        horizontal = False,
        path = "/images/Agra_141.jpg",
    )
    image_list.append(image10)

    image11 = Image(
        title = "Boise 010",
        location = "Boise, ID, USA",
        year = 2009,
        gallery = "Place",
        horizontal = False,
        path = "/images/Boise_010.jpg",
    )
    image_list.append(image11)

    image12 = Image(
        title = "Brooklyn Naval Yard 070",
        location = "Brooklyn, NY, USA",
        year = 2008,
        gallery = "Space",
        horizontal = False,
        path = "/images/brooklyn_naval_yard070.jpg",
    )
    image_list.append(image12)

    image13 = Image(
        title = "Elephant",
        location = "Cochin, Carola, India",
        year = 2010,
        gallery = "Place",
        horizontal = False,
        path = "/images/Cochin_Elephant_104.jpg",
    )
    image_list.append(image13)

    image14 = Image(
        title = "Iceland 210",
        location = "Golden Circle, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/Golden_Circle_210.jpg",
    )
    image_list.append(image14)

    image15 = Image(
        title = "Gullfoss 296",
        location = "Golden Circle, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/Golden_Circle_296.jpg",
    )
    image_list.append(image15)

    image16 = Image(
        title = "Gullfoss 303",
        location = "Golden Circle, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/Golden_Circle_303.jpg",
    )
    image_list.append(image16)

    image17 = Image(
        title = "Joshua Tree",
        location = "Joshua Tree N.P, CA, USA",
        year = 2009,
        gallery = "Place",
        horizontal = False,
        path = "/images/joshua_tree_092.jpg",
    )
    image_list.append(image17)

    image18 = Image(
        title = "Petronas Twin Towers",
        location = "Kuala Lumpur, Malaysia",
        year = 2008,
        gallery = "Space",
        horizontal = False,
        path = "/images/kuala_lumpur_075.jpg",
    )
    image_list.append(image18)

    image19 = Image(
        title = "Menara Kuala Lumpur",
        location = "Kuala Lumpur, Malaysia",
        year = 2008,
        gallery = "Space",
        horizontal = False,
        path = "/images/kuala_lumpur_081.jpg",
    )
    image_list.append(image19)

    image20 = Image(
        title = "Kuala Lumpur High Rise",
        location = "Kuala Lumpur, Malaysia",
        year = 2008,
        gallery = "Space",
        horizontal = False,
        path = "/images/kuala_lumpur_101_crop_symtcl.jpg",
    )
    image_list.append(image20)

    image21 = Image(
        title = "Menara Kuala Lumpur",
        location = "Kuala Lumpur, Malaysia",
        year = 2008,
        gallery = "Space",
        horizontal = False,
        path = "/images/kuala_lumpur_137.jpg",
    )
    image_list.append(image21)

    image22 = Image(
        title = "Lake Havasu",
        location = "Lake Havasu, AZ, USA",
        year = 2001,
        gallery = "Place",
        horizontal = False,
        path = "/images/LakeHavasu1.5.jpg",
    )
    image_list.append(image22)

    image23 = Image(
        title = "Macau 080",
        location = "Macau, PRC",
        year = 2008,
        gallery = "Place",
        horizontal = False,
        path = "/images/macau_080.jpg",
    )
    image_list.append(image23)

    image24 = Image(
        title = "Wall 209",
        location = "Paris, France",
        year = 2011,
        gallery = "Space",
        horizontal = False,
        path = "/images/Paris_209.jpg",
    )
    image_list.append(image24)

    image25 = Image(
        title = "Vending",
        location = "Rochester, NY, USA",
        year = 2006,
        gallery = "Space",
        horizontal = False,
        path = "/images/vending1_2.jpg",
    )
    image_list.append(image25)

    image26 = Image(
        title = "Westminster Arches 1.1",
        location = "Westminster, London, UK",
        year = 2008,
        gallery = "Place",
        horizontal = False,
        path = "/images/westminster_arches1-1.jpg",
    )
    image_list.append(image26)

    image27 = Image(
        title = "White Chair 1c",
        location = "Westminster, London, UK",
        year = 2008,
        gallery = "Space",
        horizontal = False,
        path = "/images/white_chair1c.jpg",
    )
    image_list.append(image27)

    image28 = Image(
        title = "Windmills 40",
        location = "Palm Springs, CA, USA",
        year = 2009,
        gallery = "Place",
        horizontal = False,
        path = "/images/windmills_040.jpg",
    )
    image_list.append(image28)

    image29 = Image(
        title = "Winterthur 028",
        location = "Winterthur, Switzerland",
        year = 2013,
        gallery = "Place",
        horizontal = False,
        path = "/images/Winterthur_028_1.jpg",
    )
    image_list.append(image29)

    image30 = Image(
        title = "Winterthur 049",
        location = "Winterthur, Switzerland",
        year = 2013,
        gallery = "Place",
        horizontal = False,
        path = "/images/Winterthur_049.jpg",
    )
    image_list.append(image30)

    image31 = Image(
        title = "Utah Great Salt Lake 056",
        location = "Utah, USA",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/20140623_Utah_Great_Salt_Lake_056.jpg",
    )
    image_list.append(image31)

    image32 = Image(
        title = "Utah Salt Flats 050",
        location = "Utah, USA",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/20140623_Utah_Salt_Flats_050.jpg",
    )
    image_list.append(image32)
    
    image34 = Image(
        title = "Istanbul 006",
        location = "Istanbul, Türkiye",
        year = 2013,
        gallery = "From-the-Hip",
        horizontal = False,
        path = "/images/20130419_Istanbul_006.jpg",
    )
    image_list.append(image34)

    image35 = Image(
        title = "CDG 442",
        location = "CDG, Paris, France",
        year = 2014,
        gallery = "Airport",
        horizontal = False,
        path = "/images/20140919_CDG_442.jpg",
    )
    image_list.append(image35)

    image36 = Image(
        title = "CDG 488",
        location = "CDG, Paris, France",
        year = 2014,
        gallery = "Airport",
        horizontal = False,
        path = "/images/20140919_CDG_488.jpg",
    )
    image_list.append(image36)

    image37 = Image(
        title = "CDG 488bw",
        location = "CDG, Paris, France",
        year = 2014,
        gallery = "Airport",
        horizontal = False,
        path = "/images/20140919_CDG_488bw.jpg",
    )
    image_list.append(image37)

    image38 = Image(
        title = "CDG 508",
        location = "CDG, Paris, France",
        year = 2014,
        gallery = "Airport",
        horizontal = False,
        path = "/images/20140919_CDG_508.jpg",
    )
    image_list.append(image38)

    image39 = Image(
        title = "Bordeaux 844",
        location = "Bordeaux, France",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/20140920_Bordeaux_844c.jpg",
    )
    image_list.append(image39)

    image40 = Image(
        title = "Chateau Smith Haut-Lafitte 642",
        location = "Bordeaux, France",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/20140920_Chateau_Smith_Haut-Lafitte_642.jpg",
    )
    image_list.append(image40)

    image41 = Image(
        title = "Paris, France 878",
        location = "Paris, France",
        year = 2014,
        gallery = "From-the-Hip",
        horizontal = False,
        path = "/images/20140920_Paris_878.jpg",
    )
    image_list.append(image41)


    image42 = Image(
        title = "Saint-Émilion, France 786",
        location = "Saint-Émilion, France",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/20140920_Saint-Emilion_786.jpg",
    )
    image_list.append(image42)


    image43 = Image(
        title = "JFK 031",
        location = "Queens, NY, USA",
        year = 2018,
        gallery = "Airport",
        horizontal = False,
        path = "/images/20180915_JFK_031.jpg",
    )
    image_list.append(image43)

    image44 = Image(
        title = "Amangiri 085",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = False,
        path = "/images/20180917_Amangiri_085.jpg",
    )
    image_list.append(image44)

    image45 = Image(
        title = "Amangiri 088",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = False,
        path = "/images/20180917_Amangiri_088.jpg",
    )
    image_list.append(image45)
    
    image46 = Image(
        title = "Amangiri 090",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = False,
        path = "/images/20180917_Amangiri_090.jpg",
    )
    image_list.append(image46)

    image47 = Image(
        title = "Amangiri 093",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = False,
        path = "/images/20180917_Amangiri_093.jpg",
    )
    image_list.append(image47)

    image48 = Image(
        title = "Amangiri 098",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = False,
        path = "/images/20180917_Amangiri_098.jpg",
    )
    image_list.append(image48)

    image49 = Image(
        title = "Amangiri 114",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = False,
        path = "/images/20180917_Amangiri_114.jpg",
    )
    image_list.append(image49)

    image50 = Image(
        title = "Amangiri 133",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = False,
        path = "/images/20180917_Amangiri_133.jpg",
    )
    image_list.append(image50)

    image51 = Image(
        title = "Amangiri 140",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = False,
        path = "/images/20180917_Amangiri_140.jpg",
    )
    image_list.append(image51)

    image52 = Image(
        title = "Harpa 352",
        location = "Reykjavîk, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/Harpa_352.jpg",
    )
    image_list.append(image52)

    image53 = Image(
        title = "Harpa 359",
        location = "Reykjavîk, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/Harpa_359.jpg",
    )
    image_list.append(image53)

    image54 = Image(
        title = "Harpa 361",
        location = "Reykjavîk, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/Harpa_361.jpg",
    )
    image_list.append(image54)

    image55 = Image(
        title = "Harpa 395",
        location = "Reykjavîk, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/Harpa_395.jpg",
    )
    image_list.append(image55)

    image56 = Image(
        title = "Hallgrímskirkja 072",
        location = "Reykjavîk, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/Reykjavik_072_alt.jpg",
    )
    image_list.append(image56)

    image57 = Image(
        title = "Harpa 161",
        location = "Reykjavîk, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/Reykjavik_161.jpg",
    )
    image_list.append(image57)

    image58 = Image(
        title = "Harpa 166",
        location = "Reykjavîk, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = False,
        path = "/images/Reykjavik_166.jpg",
    )
    image_list.append(image58)



# seed horizontal images 

    imageH1 = Image(
        title = "Seattle 054",
        location = "Seattle, WA, USA",
        year = 2012,
        gallery = "Place",
        horizontal = True,
        path = "/images/20120719_Seattle_054.jpg",
    )
    image_list.append(imageH1)

    imageH2 = Image(
        title = "Sunrise off I5",
        location = "Central CA, USA",
        year = 2013,
        gallery = "Place",
        horizontal = True,
        path = "/images/20130117_I5_002-8bit.jpg",
    )
    image_list.append(imageH2)

    imageH3 = Image(
        title = "Orchard off I5",
        location = "Central CA, USA",
        year = 2013,
        gallery = "Place",
        horizontal = True,
        path = "/images/20130307_i5_003.jpg",
    )
    image_list.append(imageH3)

    imageH4 = Image(
        title = "Breaktime",
        location = "Attaturk Airport, Istanbul, Türkiye",
        year = 2013,
        gallery = "Airport",
        horizontal = True,
        path = "/images/20130410_IST_068.jpg",
    )
    image_list.append(imageH4)

    imageH5 = Image(
        title = "St. Pancras 002",
        location = "London, England, UK",
        year = 2013,
        gallery = "Space",
        horizontal = True,
        path = "/images/20130417_London_002.jpg",
    )
    image_list.append(imageH5)

    imageH6 = Image(
        title = "St. Pancras 013",
        location = "London, England, UK",
        year = 2013,
        gallery = "Space",
        horizontal = True,
        path = "/images/20130417_London_013.jpg",
    )
    image_list.append(imageH6)

    imageH7 = Image(
        title = "London Eye View",
        location = "London, England, UK",
        year = 2013,
        gallery = "Place",
        horizontal = True,
        path = "/images/20130417_London_013.jpg",
    )
    image_list.append(imageH7)

    imageH8 = Image(
        title = "Lille 049",
        location = "Lille, France",
        year = 2013,
        gallery = "Place",
        horizontal = True,
        path = "/images/20130418_Lille_049.jpg",
    )
    image_list.append(imageH8)

    imageH9 = Image(
        title = "Lille 085",
        location = "Lille, France",
        year = 2013,
        gallery = "Space",
        horizontal = True,
        path = "/images/20130418_Lille_085.jpg",
    )
    image_list.append(imageH9)

    imageH10 = Image(
        title = "Lille 094",
        location = "Lille, France",
        year = 2013,
        gallery = "Space",
        horizontal = True,
        path = "/images/20130418_Lille_094.jpg",
    )
    image_list.append(imageH10)

    imageH11 = Image(
        title = "Grand Bazaar 009",
        location = "Istanbul, Türkiye",
        year = 2013,
        gallery = "Space",
        horizontal = True,
        path = "/images/20130419_Istanbul_009.jpg",
    )
    image_list.append(imageH11)

    imageH12 = Image(
        title = "Yeni Cami Mosque",
        location = "Istanbul, Türkiye",
        year = 2013,
        gallery = "Place",
        horizontal = True,
        path = "/images/20130420_Istanbul_106.jpg",
    )
    image_list.append(imageH12)

    imageH13 = Image(
        title = "SFO 009",
        location = "San Francisco, CA, USA",
        year = 2013,
        gallery = "Space",
        horizontal = True,
        path = "/images/20130912_SFO_009.jpg",
    )
    image_list.append(imageH13)

    imageH14 = Image(
        title = "IAD 014",
        location = "Dulles, VA, USA",
        year = 2013,
        gallery = "Space",
        horizontal = True,
        path = "/images/20131019_IAD_014.jpg",
    )
    image_list.append(imageH14)

    imageH15 = Image(
        title = "IAD 002",
        location = "Dulles, VA, USA",
        year = 2013,
        gallery = "Space",
        horizontal = True,
        path = "/images/20131021_IAD_002.jpg",
    )
    image_list.append(imageH15)

    imageH16 = Image(
        title = "IAD 009",
        location = "Dulles, VA, USA",
        year = 2013,
        gallery = "Space",
        horizontal = True,
        path = "/images/20131021_IAD_009.jpg",
    )
    image_list.append(imageH16)

    imageH17 = Image(
        title = "IAD 038",
        location = "Dulles, VA, USA",
        year = 2013,
        gallery = "Space",
        horizontal = True,
        path = "/images/20131021_IAD_038.jpg",
    )
    image_list.append(imageH17)

    imageH18 = Image(
        title = "Dune du Pilat 692",
        location = "Dune du Pilat, France",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140920_Dune_du_Pilat_692.jpg",
    )
    image_list.append(imageH18)

    imageH19 = Image(
        title = "Dune du Pilat 677",
        location = "Dune du Pilat, France",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140920_Dune_du_Pilat_677.jpg",
    )
    image_list.append(imageH19)

    imageH20 = Image(
        title = "Agra_213",
        location = "Agra, Uttar Pradesh, India",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Agra_213.jpg",
    )
    image_list.append(imageH20)

    imageH21 = Image(
        title = "Agra_275",
        location = "Agra, Uttar Pradesh, India",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Agra_275.jpg",
    )
    image_list.append(imageH21)

    imageH22 = Image(
        title = "AMC 25 4nd St",
        location = "New York, NY, USA",
        year = 2011,
        gallery = "Space",
        horizontal = True,
        path = "/images/AMC_25_42nd_St_004.jpg",
    )
    image_list.append(imageH22)

    imageH23 = Image(
        title = "Lights",
        location = "Aruba",
        year = 2009,
        gallery = "Space",
        horizontal = True,
        path = "/images/Aruba_038.jpg",
    )
    image_list.append(imageH23)

    imageH24 = Image(
        title = "Boise_154",
        location = "Boise, ID, USA",
        year = 2009,
        gallery = "Place",
        horizontal = True,
        path = "/images/Boise_154.jpg",
    )
    image_list.append(imageH24)

    imageH25 = Image(
        title = "Camel",
        location = "Rajasthan, India",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Camel_Safari_350.jpg",
    )
    image_list.append(imageH25)

    imageH26 = Image(
        title = "Red Roof",
        location = "Delhi, Uttar Pradesh, India",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Delhi_119.jpg",
    )
    image_list.append(imageH26)

    imageH27 = Image(
        title = "Golden Circle 339",
        location = "Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/Golden_Circle_339_OG.jpg",
    )
    image_list.append(imageH27)
    
    imageH28 = Image(
        title = "Lantau Island",
        location = "Lantau Island, HK, SAR of PRC",
        year = 2008,
        gallery = "Place",
        horizontal = True,
        path = "/images/hk_319.jpg",
    )
    image_list.append(imageH28)

    imageH29 = Image(
        title = "lib2.1",
        location = "Rochester, NY, USA",
        year = 2005,
        gallery = "Space",
        horizontal = True,
        path = "/images/lib2-1.jpg",
    )
    image_list.append(imageH29)

    imageH30 = Image(
        title = "lndneye1-1",
        location = "London, England, UK",
        year = 2006,
        gallery = "Place",
        horizontal = True,
        path = "/images/lndneye1-1.jpg",
    )
    image_list.append(imageH30)

    imageH31 = Image(
        title = "Fishing",
        location = "Macau, SAR of PRC",
        year = 2008,
        gallery = "Place",
        horizontal = True,
        path = "/images/macau_105.jpg",
    )
    image_list.append(imageH31)

    imageH32 = Image(
        title = "Macau Tower 127",
        location = "Macau, SAR of PRC",
        year = 2008,
        gallery = "Place",
        horizontal = True,
        path = "/images/macau_127.jpg",
    )
    image_list.append(imageH32)

    imageH33 = Image(
        title = "Macau Tower 130",
        location = "Macau, SAR of PRC",
        year = 2008,
        gallery = "Place",
        horizontal = True,
        path = "/images/macau_130.jpg",
    )
    image_list.append(imageH33)

    imageH34 = Image(
        title = "Quiet in Macau",
        location = "Macau, SAR of PRC",
        year = 2008,
        gallery = "Place",
        horizontal = True,
        path = "/images/macau_214.jpg",
    )
    image_list.append(imageH34)

    imageH35 = Image(
        title = "Meilen 029",
        location = "Meilen, Switzerland",
        year = 2011,
        gallery = "Place",
        horizontal = True,
        path = "/images/Meilen_029.jpg",
    )
    image_list.append(imageH35)

    imageH36 = Image(
        title = "Meilen 038",
        location = "Meilen, Switzerland",
        year = 2011,
        gallery = "Place",
        horizontal = True,
        path = "/images/Meilen_038.jpg",
    )
    image_list.append(imageH36)

    imageH37 = Image(
        title = "Oregon Coast 017",
        location = "OR, USA",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Oregon_Coast_017.jpg",
    )
    image_list.append(imageH37)

    imageH38 = Image(
        title = "Oregon Coast 026",
        location = "OR, USA",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Oregon_Coast_026.jpg",
    )
    image_list.append(imageH38)

    imageH39 = Image(
        title = "Oregon Coast 032",
        location = "Oregon Coast, USA",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Oregon_Coast_032.jpg",
    )
    image_list.append(imageH39)
    
    imageH40 = Image(
        title = "Oregon_Coast_151",
        location = "OR, USA",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Oregon_Coast_151.jpg",
    )
    image_list.append(imageH40)
    
    imageH41 = Image(
        title = "Pondicherry 160",
        location = "Puducherry, Union Territory, India",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Pondy_160.jpg",
    )
    image_list.append(imageH41)

    imageH42 = Image(
        title = "Rheinfall 087",
        location = "Switzerland",
        year = 2011,
        gallery = "Place",
        horizontal = True,
        path = "/images/Rheinfall_087.jpg",
    )
    image_list.append(imageH42)

    imageH43 = Image(
        title = "Rüschlikon 022",
        location = "Rüschlikon, Switzerland",
        year = 2013,
        gallery = "Place",
        horizontal = True,
        path = "/images/Ruschlikon_022bw.jpg",
    )
    image_list.append(imageH43)
    
    imageH44 = Image(
        title = "Säntis 036",
        location = "Switzerland",
        year = 2011,
        gallery = "Place",
        horizontal = True,
        path = "/images/Santis_036.jpg",
    )
    image_list.append(imageH44)
    
    imageH45 = Image(
        title = "Appenzeller Schaukäserei 011",
        location = "Switzerland",
        year = 2011,
        gallery = "Place",
        horizontal = True,
        path = "/images/Schaukaserei_011.jpg",
    )
    image_list.append(imageH45)

    imageH46 = Image(
        title = "Seattle Space Needle 003",
        location = "Seattle, WA, USA",
        year = 2009,
        gallery = "Place",
        horizontal = True,
        path = "/images/Seattle_003.jpg",
    )
    image_list.append(imageH46)

    imageH47 = Image(
        title = "Midtown Manhattan from L.I.C",
        location = "Queens, NY, USA",
        year = 2006,
        gallery = "Place",
        horizontal = True,
        path = "/images/un_9hrz_1_2.jpg",
    )
    image_list.append(imageH47)

    imageH48 = Image(
        title = "Windmills 63",
        location = "Palm Springs, CA, USA",
        year = 2009,
        gallery = "Place",
        horizontal = True,
        path = "/images/windmills_063.jpg",
    )
    image_list.append(imageH48)

    imageH49 = Image(
        title = "SFO 002",
        location = "SFO, South San Francisco, CA, USA",
        year = 2013,
        gallery = "Airport",
        horizontal = True,
        path = "/images/20130912_SFO_002.jpg",
    )
    image_list.append(imageH49)

    imageH50 = Image(
        title = "Great Salt Lake 055",
        location = "UT, USA",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140623_Utah_Great_Salt_Lake_055.jpg",
    )
    image_list.append(imageH50)

    imageH51 = Image(
        title = "Utah Salt Flats 039",
        location = "UT, USA",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140623_Utah_Salt_Flats_039.jpg",
    )
    image_list.append(imageH51)

    imageH52 = Image(
        title = "Utah Salt Flats 048",
        location = "UT, USA",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140623_Utah_Salt_Flats_048.jpg",
    )
    image_list.append(imageH52)

    imageH53 = Image(
        title = "Utah Salt Flats 049",
        location = "UT, USA",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140623_Utah_Salt_Flats_049.jpg",
    )
    image_list.append(imageH53)

    imageH54 = Image(
        title = "Zion National Park 076",
        location = "UT, USA",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140623_Utah_Zion_NP_076.jpg",
    )
    image_list.append(imageH54)

    imageH55 = Image(
        title = "Zion National Park 095",
        location = "UT, USA",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140623_Utah_Zion_NP_095.jpg",
    )
    image_list.append(imageH55)

    imageH56 = Image(
        title = "CDG 454",
        location = "CDG, Paris, France",
        year = 2014,
        gallery = "Airport",
        horizontal = True,
        path = "/images/20140919_CDG_454bw.jpg",
    )
    image_list.append(imageH56)

    imageH57 = Image(
        title = "CDG 457",
        location = "CDG, Paris, France",
        year = 2014,
        gallery = "Airport",
        horizontal = True,
        path = "/images/20140919_CDG_457.jpg",
    )
    image_list.append(imageH57)

    imageH58 = Image(
        title = "CDG 513",
        location = "CDG, Paris, France",
        year = 2014,
        gallery = "Airport",
        horizontal = True,
        path = "/images/20140919_CDG_513.jpg",
    )
    image_list.append(imageH58)

    imageH59 = Image(
        title = "Chateaux Haut-Bailly 538",
        location = "Bordeaux, France",
        year = 2014,
        gallery = "Space",
        horizontal = True,
        path = "/images/20140920_Chateau_Haut_Bailly_538.jpg",
    )
    image_list.append(imageH59)

    imageH60 = Image(
        title = "Saint-Émilion, France 729",
        location = "Saint-Émilion, France",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140920_Saint-Emilion_729.jpg",
    )
    image_list.append(imageH60)

    imageH61 = Image(
        title = "Saint-Émilion, France 736",
        location = "Saint-Émilion, France",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140920_Saint-Emilion_736.jpg",
    )
    image_list.append(imageH61)

    imageH62 = Image(
        title = "Saint-Émilion, France 793",
        location = "Saint-Émilion, France",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140920_Saint-Emilion_793.jpg",
    )
    image_list.append(imageH62)

    imageH63 = Image(
        title = "JFK 001",
        location = "JFK, Queens, NY, USA",
        year = 2018,
        gallery = "Airport",
        horizontal = True,
        path = "/images/20180915_JFK_001.jpg",
    )
    image_list.append(imageH63)

    imageH64 = Image(
        title = "JFK 038",
        location = "JFK, Queens, NY, USA",
        year = 2018,
        gallery = "Airport",
        horizontal = True,
        path = "/images/20180915_JFK_038.jpg",
    )
    image_list.append(imageH64)

    imageH65 = Image(
        title = "Page, AZ 044",
        location = "Page, AZ, USA",
        year = 2018,
        gallery = "Place",
        horizontal = True,
        path = "/images/20180916_Page-AZ_044.jpg",
    )
    image_list.append(imageH65)

    imageH66 = Image(
        title = "Page, AZ 047",
        location = "Page, AZ, USA",
        year = 2018,
        gallery = "Place",
        horizontal = True,
        path = "/images/20180916_Page-AZ_047.jpg",
    )
    image_list.append(imageH66)

    imageH67 = Image(
        title = "Page, AZ 048",
        location = "Page, AZ, USA",
        year = 2018,
        gallery = "Place",
        horizontal = True,
        path = "/images/20180916_Page-AZ_048.jpg",
    )
    image_list.append(imageH67)

    imageH68 = Image(
        title = "Amangiri 067",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Space",
        horizontal = True,
        path = "/images/20180917_Amangiri_067.jpg",
    )
    image_list.append(imageH68)

    imageH69 = Image(
        title = "Amangiri 069",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Space",
        horizontal = True,
        path = "/images/20180917_Amangiri_069.jpg",
    )
    image_list.append(imageH69)

    imageH70 = Image(
        title = "Amangiri 080",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Space",
        horizontal = True,
        path = "/images/20180917_Amangiri_080.jpg",
    )
    image_list.append(imageH70)

    imageH71 = Image(
        title = "Amangiri 082",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Space",
        horizontal = True,
        path = "/images/20180917_Amangiri_082.jpg",
    )
    image_list.append(imageH71)

    imageH72 = Image(
        title = "Amangiri 101",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Space",
        horizontal = True,
        path = "/images/20180917_Amangiri_101.jpg",
    )
    image_list.append(imageH72)

    imageH73 = Image(
        title = "Amangiri 103",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = True,
        path = "/images/20180917_Amangiri_103.jpg",
    )
    image_list.append(imageH73)

    imageH74 = Image(
        title = "Amangiri 109",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = True,
        path = "/images/20180917_Amangiri_109.jpg",
    )
    image_list.append(imageH74)

    imageH75 = Image(
        title = "Amangiri 127",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Space",
        horizontal = True,
        path = "/images/20180917_Amangiri_127.jpg",
    )
    image_list.append(imageH75)

    imageH76 = Image(
        title = "Amangiri 154",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = True,
        path = "/images/20180917_Amangiri_154.jpg",
    )
    image_list.append(imageH76)

    imageH77 = Image(
        title = "Amangiri 156",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Place",
        horizontal = True,
        path = "/images/20180917_Amangiri_156.jpg",
    )
    image_list.append(imageH77)

    imageH78 = Image(
        title = "Amangiri 158",
        location = "Canyon Point, UT, USA",
        year = 2018,
        gallery = "Space",
        horizontal = True,
        path = "/images/20180917_Amangiri_158.jpg",
    )
    image_list.append(imageH78)

    imageH79 = Image(
        title = "Iceland 175",
        location = "Golden Circle, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/Golden_Circle_175.jpg",
    )
    image_list.append(imageH79)

    imageH80 = Image(
        title = "Iceland 204",
        location = "Golden Circle, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/Golden_Circle_204.jpg",
    )
    image_list.append(imageH80)

    imageH81 = Image(
        title = "Iceland 220",
        location = "Golden Circle, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/Golden_Circle_220.jpg",
    )
    image_list.append(imageH81)

    imageH82 = Image(
        title = "Iceland 322",
        location = "Golden Circle, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/Golden_Circle_322.jpg",
    )
    image_list.append(imageH82)

    imageH83 = Image(
        title = "Iceland 339",
        location = "Golden Circle, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/Golden_Circle_339.jpg",
    )
    image_list.append(imageH83)

    imageH84 = Image(
        title = "Harpa 364",
        location = "Reykjavik, Iceland",
        year = 2014,
        gallery = "Space",
        horizontal = True,
        path = "/images/Harpa_364.jpg",
    )
    image_list.append(imageH84)

    imageH85 = Image(
        title = "Harpa 375",
        location = "Reykjavik, Iceland",
        year = 2014,
        gallery = "Space",
        horizontal = True,
        path = "/images/Harpa_375.jpg",
    )
    image_list.append(imageH85)

    imageH86 = Image(
        title = "Harpa 381",
        location = "Reykjavik, Iceland",
        year = 2014,
        gallery = "Space",
        horizontal = True,
        path = "/images/Harpa_381.jpg",
    )
    image_list.append(imageH86)

    imageH87 = Image(
        title = "Hallgrimskirka 094",
        location = "Reykjavik, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/Reykjavik_094.jpg",
    )
    image_list.append(imageH87)

    imageH88 = Image(
        title = "Hallgrimskirka 107",
        location = "Reykjavik, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/Reykjavik_107.jpg",
    )
    image_list.append(imageH88)

    imageH89 = Image(
        title = "Harpa 171",
        location = "Reykjavik, Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/Reykjavik_171.jpg",
    )
    image_list.append(imageH89)

    # print(image_list)

    try:
        db.session.add_all(image_list)
        db.session.commit()
        print(f"Successfuly added {len(image_list)} images to the database")
    except Exception as e:
        print(f"Error adding images: {e}")
        db.session.rollback()

    
    # print("Db seed complete - now it's entirely up to you!!")

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed process...")
        seed_data()
