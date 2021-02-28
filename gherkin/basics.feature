# Gherkin basics
# Gherkin tutorials of the basics needed to get started


# WHEN:
# Gherkin was developed by Dan North in the 2000s.

# WHAT:
# Gherkin scripts connect the human concept of cause and effect to the software concepts of input/process/output

# WHY:
# Dan was looking for a simple and elegant way to describe behavior at the application level


# There are three components to a gherkin script that relate to the input/process/output of an intended program:
# 1. Given - relates to input
# 2. When - relates to the process
# 3. Then - relates to output


#-----------------------------------------------------------------------------------------------------------------
# GIVEN - Some refer to this step as "preconditions to the action". THe purpose of the Given steps is to
# put the system in a known state before the user or external system starts interacting with the system


#-----------------------------------------------------------------------------------------------------------------
# WHEN - The purpose of the When steps are to describe the key action the user performs.


#-----------------------------------------------------------------------------------------------------------------
# THEN - The Then steps are the expected results of the When steps. Its purpose is to observe the outcome of the previous action.
# Many times the outcome is some kind of output; something that comes out of the system that we are looking for
# This might be a report, a message, navigation to a page, etc.
# Other times it might be data in a database that has changed or the output from a web service. Either way, it can be quantified. Some examples:

#-----------------------------------------------------------------------------------------------------------------

# conclusion

# The power of a well-written Gherkin script is that it facilitates the conversation to make sure it is right.

