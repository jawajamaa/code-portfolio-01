#!/usr/bin/env python3

# local imports
from app import app
from models import db, Image

def seed_data():

    print("Deleting all previous data...")
    Image.query.delete()

# seed mobile wallpaper 
    print("adding Images...")
    image_list =[]

    image1 = Image(
        title = "SLO",
        location = "San Luis Obispo, CA, USA",
        year = 2012,
        gallery = "Space",
        horizontal = False,
        path = "/images/120428_SLO_076.jpg",
    )
    image_list.append(image1)

    image2 = Image(
        title = "Lille 26",
        location = "Lille, France",
        year = 2013,
        gallery = "Place",
        horizontal = False,
        path = "/images/20130418_Lille_26c.jpg",
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
        location = "Istanbul, Turkey",
        year = 2013,
        gallery = "From-the-Hip",
        horizontal = False,
        path = "/images/20130419_Istanbul_003.jpg",
    )
    image_list.append(image4)

    image5 = Image(
        title = "Istanbul 070",
        location = "Istanbul, Turkey",
        year = 2013,
        gallery = "Place",
        horizontal = False,
        path = "/images/20130419_Istanbul_070.jpg",
    )
    image_list.append(image5)

    image6 = Image(
        title = "Istanbul 038",
        location = "Istanbul, Turkey",
        year = 2013,
        gallery = "Place",
        horizontal = False,
        path = "/images/20130420_Istanbul_0038.jpg",
    )
    image_list.append(image6)

    image7 = Image(
        title = "Istanbul 117",
        location = "Istanbul, Turkey",
        year = 2013,
        gallery = "From-the-Hip",
        horizontal = False,
        path = "/images/20130420_Istanbul_117_nc.jpg",
    )
    image_list.append(image7)

    image8 = Image(
        title = "IAD 003",
        location = "Washington, D.C, USA",
        year = 2013,
        gallery = "Airport",
        horizontal = False,
        path = "/images/20131019_IAD_003.jpg",
    )
    image_list.append(image8)

    image9 = Image(
        title = "Dune du Pilat 682",
        location = "Dune du Pilat, France",
        year = 2013,
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
        location = "Boise, Idaho, USA",
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
        title = "Orchard off i5 003",
        location = "Central CA, USA",
        year = 2013,
        gallery = "Place",
        horizontal = True,
        path = "/images/20130307_i5_003.jpg",
    )
    image_list.append(imageH2)

    imageH3 = Image(
        title = "Dune du Pilat 692",
        location = "Dune du Pilat, France",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140920_Dune_du_Pilat_692.jpg",
    )
    image_list.append(imageH3)

    imageH4 = Image(
        title = "Dune du Pilat 677",
        location = "Dune du Pilat, France",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140920_Dune_du_Pilat_677.jpg",
    )
    image_list.append(imageH4)

    imageH5 = Image(
        title = "Windmills 63",
        location = "Palm Springs, CA, USA",
        year = 2009,
        gallery = "Place",
        horizontal = True,
        path = "/images/windmills_063.jpg",
    )
    image_list.append(imageH5)

    imageH6 = Image(
        title = "Midtown Manhattan from L.I.C",
        location = "Queens, NY, USA",
        year = 2006,
        gallery = "Place",
        horizontal = True,
        path = "/images/un_9hrz_1_2.jpg",
    )
    image_list.append(imageH6)

    imageH7 = Image(
        title = "Seattle Space Needle 003",
        location = "Seattle, WA, USA",
        year = 2009,
        gallery = "Place",
        horizontal = True,
        path = "/images/Seattle_003.jpg",
    )
    image_list.append(imageH7)

    imageH8 = Image(
        title = "Meilen 029",
        location = "Meilen, Switzerland",
        year = 2011,
        gallery = "Place",
        horizontal = True,
        path = "/images/Meilen_029.jpg",
    )
    image_list.append(imageH8)

    imageH9 = Image(
        title = "Meilen 038",
        location = "Meilen, Switzerland",
        year = 2011,
        gallery = "Place",
        horizontal = True,
        path = "/images/Meilen_038.jpg",
    )
    image_list.append(imageH9)

    imageH10 = Image(
        title = "macau_105",
        location = "Macau, SAR of PRC",
        year = 2008,
        gallery = "Place",
        horizontal = True,
        path = "/images/macau_105.jpg",
    )
    image_list.append(imageH10)

    imageH11 = Image(
        title = "macau_127",
        location = "Macau, SAR of PRC",
        year = 2008,
        gallery = "Place",
        horizontal = True,
        path = "/images/macau_127.jpg",
    )
    image_list.append(imageH11)

    imageH12 = Image(
        title = "macau_130",
        location = "Macau, SAR of PRC",
        year = 2006,
        gallery = "Place",
        horizontal = True,
        path = "/images/macau_130.jpg",
    )
    image_list.append(imageH12)

    imageH13 = Image(
        title = "hk 319",
        location = "Lantau Island, HK, SAR of PRC",
        year = 2008,
        gallery = "Place",
        horizontal = True,
        path = "/images/hk_319.jpg",
    )
    image_list.append(imageH13)

    imageH14 = Image(
        title = "Golden_Circle_339_OG",
        location = "Iceland",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/Golden_Circle_339_OG.jpg",
    )
    image_list.append(imageH14)

    imageH15 = Image(
        title = "Camel_Safari_350",
        location = "Rajasthan, India",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Camel_Safari_350.jpg",
    )
    image_list.append(imageH15)

    imageH16 = Image(
        title = "Oregon_Coast_032",
        location = "Oregon Coast, USA",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Oregon_Coast_032.jpg",
    )
    image_list.append(imageH16)

    imageH17 = Image(
        title = "Rheinfall_087",
        location = "Switzerland",
        year = 2011,
        gallery = "Place",
        horizontal = True,
        path = "/images/Rheinfall_087.jpg",
    )
    image_list.append(imageH17)

    imageH18 = Image(
        title = "Agra_275",
        location = "Agra, Uttar Pradesh, India",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Agra_275.jpg",
    )
    image_list.append(imageH18)

    imageH19 = Image(
        title = "Agra_213",
        location = "Agra, Uttar Pradesh, India",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Agra_213.jpg",
    )
    image_list.append(imageH19)

    imageH20 = Image(
        title = "Oregon_Coast_151",
        location = "OR, USA",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Oregon_Coast_151.jpg",
    )
    image_list.append(imageH20)

    imageH21 = Image(
        title = "lndneye1-1",
        location = "London, UK",
        year = 2005,
        gallery = "Place",
        horizontal = True,
        path = "/images/lndneye1-1.jpg",
    )
    image_list.append(imageH21)
    
    imageH22 = Image(
        title = "lib2.1",
        location = "Rochester, NY, USA",
        year = 2008,
        gallery = "Space",
        horizontal = True,
        path = "/images/lib2-1.jpg",
    )
    image_list.append(imageH22)

    imageH23 = Image(
        title = "Boise_154",
        location = "Boise, ID, USA",
        year = 2009,
        gallery = "Place",
        horizontal = True,
        path = "/images/Boise_154.jpg",
    )
    image_list.append(imageH23)

    imageH24 = Image(
        title = "Oregon Coast 017",
        location = "OR, USA",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Oregon_Coast_017.jpg",
    )
    image_list.append(imageH24)

    imageH25 = Image(
        title = "Dune du Pilat 688",
        location = "Dune du Pilat, France",
        year = 2014,
        gallery = "Place",
        horizontal = True,
        path = "/images/20140920_Dune_du_Pilat_668.jpg",
    )
    image_list.append(imageH25)

    imageH26 = Image(
        title = "Säntis 036",
        location = "Switzerland",
        year = 2011,
        gallery = "Place",
        horizontal = True,
        path = "/images/Santis_036.jpg",
    )
    image_list.append(imageH26)

    imageH27 = Image(
        title = "Oregon Coast 026",
        location = "OR, USA",
        year = 2010,
        gallery = "Place",
        horizontal = True,
        path = "/images/Oregon_Coast_026.jpg",
    )
    image_list.append(imageH27)

    db.session.add_all(image_list)
