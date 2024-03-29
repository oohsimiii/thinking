# coding: utf-8
from charity_models import Charity
import sys
sys.setrecursionlimit(2000)

def seed_data():
    C1_key = Charity(charity_name = "Singapore Children's Society", link = "https://www.childrensociety.org.sg/").put()
    C2_key = Charity(charity_name = "Club Rainbow", link = "https://clubrainbow.squarespace.com/").put()
    C3_key = Charity(charity_name = "MILK (Mainly I Love Kids) Fund", link = "http://www.milk.org.sg/" ).put()
    C4_key = Charity(charity_name = "Children's Wishing Well", link = "https://www.wishingwell.org.sg/" ).put()
    C5_key = Charity(charity_name = "Children's Aid Society", link ="http://childrensaidsociety.org.sg/cas/" ).put()
    C6_key = Charity(charity_name = "Metta Welfare Association", link = "https://www.metta.org.sg/hq/index.php/you-can-help/").put()
    C7_key = Charity(charity_name = "Lions Home for the Elders", link = "https://lionshome.org.sg/").put()
    C8_key = Charity(charity_name = "Caregiving Welfare Association", link = "http://www.cwa.org.sg/").put()
    C9_key = Charity(charity_name = "Fei Yue", link ="http://fycs.org/" ).put()
    C10_key = Charity(charity_name = "Riding for the Disable Association Singapore", link = "http://rdasingapore.org/").put()
    C11_key = Charity(charity_name = "Very Special Arts Singapore", link = "https://www.facebook.com/vsa.singapore/").put()
    C12_key = Charity(charity_name = "Movement for the Intellectually Disabled of Singapore (MINDS)", link ="http://www.minds.org.sg/" ).put()
    C13_key = Charity(charity_name = "Oasis Second Chance Animal Shelter (OSCAS)", link = "http://www.oscas.sg/").put()
    C14_key = Charity(charity_name = "Action for Singapore Dogs", link = "http://asdsingapore.com/wp/").put()
    C15_key = Charity(charity_name = "Society for the Prevention of Cruelty to Animals (SPCA)", link = "http://www.spca.org.sg/").put()
    C16_key = Charity(charity_name = "Babes", link ="http://babes.org.sg/" ).put()
    C17_key = Charity(charity_name = "Singapore Council of Women's Organisations", link ="https://www.scwo.org.sg/" ).put()
    C18_key = Charity(charity_name = "Aidha", link = "http://www.aidha.org/").put()
    C19_key = Charity(charity_name = "Association of Women for Action and Research (AWARE)", link = "http://www.aware.org.sg/register/volunteer-centre/").put()
    C20_key = Charity(charity_name = "Asian Women's Welfare Association (AWWA)", link ="https://www.awwa.org.sg/" ).put()
    C21_key = Charity(charity_name = "ONE (Singapore)", link ="http://onesingapore.org/" ).put()
    C22_key = Charity(charity_name = "TOUCH Community Services", link = "https://www.touch.org.sg/").put()
    C23_key = Charity(charity_name = "Singapore Red Cross Society", link = "http://www.redcross.org.sg/").put()
