from story import Concept, Object

accused = Concept(2)
accused_of_being_con_artist = Concept(2)
acted_desperate_for_romance = Concept(1, "actedDesperateForRomance")
altered_the_deal = Concept(2) # 1st one altered deal between the two
asked_after_father = Concept(2, "askedAfterFather")
asked_dog_to_find_keys = Concept(1, "askedDogToFindKeys")
died = Concept(1, "died")
found_keys = Concept(1, "foundKeys")
found_motive = Concept(1, "foundMotive")
got_arrested = Concept(1, "gotArrested")

has_a_gun_concept = Concept(1, "hasAGun", num_value_parameters=1)
has_a_gun_obj = Object("has_a_gun")
has_no_gun_obj = Object("has_no_gun")
def has_a_gun(character):
    return has_a_gun_concept.current([character], [has_a_gun_obj])
def has_no_gun(character):
    return has_a_gun_concept.current([character], [has_no_gun_obj])

has_a_case = Concept(1, "hasACase")
has_appointment_tomorrow_morning = Concept(1)
has_flimsy_evidence_against = Concept(2)
has_guidance = Concept(2, "hasGuidance") # 1st param is the PI, 2nd is mentor
heard_coded_words = Concept(1, "heardCodedWords")
heard_secret_message_from_singer = Concept(1, "heardSecretMessageFromSinger")

#TODO: these should be stateful
isChainedUp = Concept(1, "isChainedUp")
isFree = Concept(1, "isFree")

is_charmed_by = Concept(2)

is_eager_to_take_case = Concept(1)
is_injured_in_hospital = Concept(1)
kicked_out_client = Concept(2, "kickedOutClient")

# 1 made 2 uncomfortable while being well aware of what they were doing.
knowingly_made_uncomfortable = Concept(2)

knows_burglars_hung_out_at_bar = Concept(1, "knowsBurglarsHungOutAtBar")
knows_father_hung_out_at_bar = Concept(1, "knowsFatherHungOutAtBar")
knows_father_met_with = Concept(2, "knowsFatherMetWith")
knows_is_creepy = Concept(2) # 1st knows 2nd is creepy
knows_perp_is_in_chinatown = Concept(1, "knowIsInChinatown")
knows_to_check_out_docks = Concept(1)

made_incorrect_public_accusation = Concept(1)
made_a_deal = Concept(2)

# The missing father is not the reason this person has come here.
missing_father_is_not_reason_for_being_here = Concept(1)
saw_missing_father_head_to_bar = Concept(1, "sawMissingFatherHeadToBar")
started_phone_call_to = Concept(2)
suggested_father_smuggled_drugs = Concept(1)

talking_to_concept = Concept(
    1, "talkingTo", num_value_parameters=1
)
def talking_to(character1, character2):
    return talking_to_concept.current([character1], [character2])

talking_on_phone_concept = Concept(
    1, "talkingOnPhone", num_value_parameters=1
)
def talking_on_phone(character1, character2):
    return talking_on_phone_concept.current([character1], [character2])

told_to_focus_on_where_people_are = Concept(1, "toldToFocusOnWherePeopleAre")
told_to_go_smoke_weed = Concept(1)
tripping = Concept(1, "tripping")
tripyExistentialCrisis = Concept(1, "tripyExistentialCrisis")

wants_to_see_something_happen_tomorrow_morning = Concept(1)
was_awkward_to = Concept(1)
was_in_traumatic_awkward_situation = Concept(
    1, "wasInTraumaticAwkwardSituation"
)
