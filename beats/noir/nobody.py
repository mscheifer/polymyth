from story import Object

#TODO: instead of this, add the ability to unset the concept value.
# But long term should have the engine support a time concept. What we care
# about is:
#  1. Has something ever happend (can easily put any1 in the time param) or a
#  a bound param that isn't used anywhere else.
#  2. Has something happened before something else (this needs a special
#  operator like are_different).
#  3. Did two things happen simultaneously. (This needs a special operator too)
#  (This is probably a rarer use case than the ordering one)
#  4. To facilitate this we need a special object that creates a new 'moment'
#  that is considered to be after every beat that came before. But we also want
#  to establish that something happened in the past sometimes, which means we
#  nned the ability to create a new moment but also establish that is before
#  another moment. We could do that by letting the special happens_before op be
#  used in the _sets_up part of the rule.
nobody = Object("nobody")

