from story import Concept, Object

# These are used if you have something where the reader would complain if it
# did not pay off ("why was she acting all suspicious? Why was this never
# explained?"). Normal concepts don't need to be here if them not directly
# leading to something wouldn't be noticed by the reader otherwise, like
# tonal background details. Stuff that directly contributes to the plot/arcs
# would also elicit this response from readers but is handled with more specific
# structure in those files. So these concepts aren't needed on top of that.
needs_payoff = Concept(1)
payed_off = Concept(1)

# TODO: I think I want to even replace the main logic that makes sure
# every established concept has lead to something with this. We
# don't actually need every single concept established go somewhere,
# only the ones that the audience would expect like I said above.
# But would we need something to prevent whole beats that don't have
# any of their concepts used? Like it would definitely be bad if we
# just had random beats that could come in or not, just making the
# story longer and adding detail that could be trimmed.
