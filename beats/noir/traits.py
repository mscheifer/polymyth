from story import Concept, MakeAntiLogic

# Generally for these concepts, they can be established by one example and then
# other beats will take them into account implying that it's an existing part of
# the character. These should be phrased as eternal traits because even as we
# change our past is still a part of us that we learn to live with. We can only
# direct our shadows to become true archetypes, we can't ignore them. For
# example: a character is still an alcoholic if they have quit drinking because
# staying sober is something they have to keep up, every day.
are_friends = Concept(2, "areFriends")
can_find_keys = Concept(1, "canFindKeys")
can_lie = Concept(1, "canLie")
can_understand_why_one_would_do_their_friend_a_favor = Concept(1)
has_dead_brother = Concept(1, "deadBro")
has_power_over = Concept(2, "hasPowerOver")
is_amnesiac = Concept(1, "isAmnesiac")
is_asshole = Concept(1, "isAsshole")
is_awkward = Concept(1, "isAwkward")
is_bold = Concept(1, "isBold")
is_cocky = Concept(1, "isCocky")
is_con_artist = Concept(1, "isConArtist")
is_creepy = Concept(1, "isCreepy")
is_client = Concept(1, "isClient")
is_father_of = Concept(2, "isFatherOf") # 1st is dad, 2nd is kid
is_fathers_secretary = Concept(1, "isFathersSecretary")
is_fathers_business_partner = Concept(1, "isFathersBusinessPartner")
is_gambler = Concept(1, "isGambler")
is_gangster = Concept(1, "isGangster")
is_goddess_archetype = Concept(1, "isGoddessArchetype")
is_honest = Concept(1, "isHonest")
is_insecure = Concept(1, "isInsecure")
is_inconsiderate = Concept(1, "isInconsiderate")
is_mother_of = Concept(2, "isMotherOf") # 1st is mom, 2nd is kid
isObsessive = Concept(1, "isObessive")
is_old_boss = Concept(1, "isOldBoss")
isParanoid = Concept(1, "isParanoid")
is_pi = Concept(1, "isPI")
is_perp = Concept(1, "isPerp")
is_potential_client = Concept(1, "isPotentialClient")
is_protag = Concept(1, "isProtag")
is_psychopathic = Concept(1, "isPsychopathic")
is_ramen_shop_owner = Concept(1, "isRamenShopOwner")
is_smoker = Concept(1, "isSmoker") # This means they have a death wish
is_regular = Concept(1, "isRegular")
is_victim = Concept(1, "isVictim")
is_violent = Concept(1, "isViolent")
know_each_other = Concept(2)
lives_with = Concept(2, "livesWith")
was_married_before = Concept(1, "wasMarriedBefore")
were_very_close = Concept(2)

# These two concepts are opposites and usually only one or the other should be
# true for a character.
needs_hard_facts_to_feel_they_understand_a_situation = Concept(1)
needs_to_know_how_everyone_feels_to_feel_they_understand_a_situation = Concept(
    1
)

anti_logic = [
    MakeAntiLogic("Can't be cocky and awkward")
        .ok_if(is_awkward(1))
        .cant_set_up(is_cocky(1)),

    MakeAntiLogic("Can't be cocky and awkward")
        .ok_if(is_cocky(1))
        .cant_set_up(is_awkward(1)),
]
