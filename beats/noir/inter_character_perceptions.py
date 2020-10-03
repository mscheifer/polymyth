from story import Concept

# These concepts are not set from the beginning of time. They can come about due
# to events in the story.

# TODO I'm thinking more and more that we'll need to unify objects and concepts
# to have arbitrary nesting and composing of anything.
#   knows = Concept(2) # 1st arg is character, 2nd is any concept
# With one declaration we can have a way to track which characters know what.

are_attracted_to_each_other = Concept(2)

have_met_before = Concept(2, "haveMetBefore")
is_attracted_to = Concept(2) # 1st is attracted to 2nd
is_suspicious_of = Concept(2, "isSuspiciousOf")
knows_father_of_1_is_missing = Concept(2)
knows_talks_a_lot = Concept(2, "knowsTalksALot")
saw_has_no_wedding_ring_on = Concept(2, "knowsTalksALot")
trusts = Concept(2, "trusts") # 1st trusts 2nd
