from story import Concept

class ProtagonistDefinition:
    want = Concept(0, "want")
    need = Concept(0, "need")
    # The lie is what makes the character want the want and prevents them from
    # knowing they need the need
    lie = Concept(0, "lie")
    # The ghost is what makes the character believe the lie
    ghost = Concept(0, "ghost")

# The journey steps, these concepts are established at the END of each section
class HerosJourney:
    you = Concept(0, "You") # get audience to identify with protag
    need = Concept(0, "Need") # Establish need
    go = Concept(0, "Go") # cross threshold
    search = Concept(0, "Search")
    find = Concept(0, "Find") # aka midpoint or meeting with the goddess
    take = Concept(0, "Take")
    # cross threshold back (rescue from without + magic flight)
    theReturn = Concept(0, "Return")
    change = Concept(0, "Change")

# Character arcs =========

# Postive
# 1. Goal - What they want (to accomplish)
# 2. Lie - Belief that they cannot accomplish goal (e.g. they are not good enough, the world is too cruel)
# 3. Truth - Learn that they can accomplish goal (e.g. learn to believe in themself, the world actually has nice people)

# By overcoming the lie, characters can move to a new role in life, overcome negative internal trait like fear

# Negative
# 1. Goal - What they want (to accomplish)
# 2. Lie - Belief that they will bring about positive change by achieving what they want
# 3. Truth - Realizing that that action did not bring about positive change


# One example:
# Goal: Have purpose in live. Get over existential malaise
# Lie: Can keep doing what they're doing and will figure it out.
# Truth: Realizes they are acting out of habit ("I just hang out with my firends out of habit"). Must take drastic action.

# The Conservative character arc as understood by conservatives
# 1. The child who belives it is their duty to help everyone
# 2. The adult who only looks out for themselves (because there is no guarantee
# that trying to help, sacrificing something, will be productive).
# 3. The grandfather who does not begrude others for not helping (because of an
# empathetic understanding of the above.
