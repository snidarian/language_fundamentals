
Gherkin is the language that Cucumber uses to define test cases. It is designed to be non-technical and human readable, and collectively describes use cases relating to a software system.[7][8][21][22] The purpose behind Gherkin's syntax is to promote behavior-driven development practices across an entire development team, including business analysts and managers. It seeks to enforce firm, unambiguous requirements starting in the initial phases of requirements definition by business management and in other stages of the development lifecycle.

In addition to providing a script for automated testing, Gherkin's natural language syntax is designed to provide simple documentation of the code under test.[22] Gherkin currently supports keywords in dozens of languages.[22][23][7][8]

Language Operations[22]

# List available languages
cucumber --i18n help

# List a language's keywords
cucumber --i18n $LANG

Syntax

Syntax is centered around a line-oriented design, similar to that of Python. The structure of a file is defined using whitespace and other control characters.[22] # is used as the line-comment character, and can be placed anywhere in a file.[22] Instructions are any non-empty and non-comment line. They consist of a recognized Gherkin keyword followed by a string.[24]

All Gherkin files have the .feature file extension. They contain a single Feature definition for the system under test and are an executable test script.[24]
Features, scenarios, and steps

Cucumber tests are divided into individual Features. These Features are subdivided into Scenarios, which are sequences of Steps.
Features

A feature is a Use Case that describes a specific function of the software being tested. There are three parts to a Feature[24]

    The Feature: keyword
    The Feature name (on the same line as the keyword)
    An optional description on the following lines

Example Feature definition

Feature: Withdraw Money from ATM

    A user with an account at a bank would like to withdraw money from an ATM.

    Provided he has a valid account and debit or credit card, he should be allowed to make the transaction. The ATM will tend the requested amount of money, return his card, and subtract amount of the withdrawal from the user's account.

    Scenario: Scenario 1
        Given preconditions
        When actions
        Then results

    Scenario: Scenario 2
        ...

Scenarios

Each Feature is made of a collection of scenarios. A single scenario is a flow of events through the Feature being described and maps 1:1 with an executable test case for the system.[24] Keeping with the example ATM withdrawal feature, a scenario might describe how a user requests money and what happens to their account.

Scenario: Eric wants to withdraw money from his bank account at an ATM
    Given Eric has a valid Credit or Debit card
    And his account balance is $100
    When he inserts his card
    And withdraws $45
    Then the ATM should return $45
    And his account balance is $55

In some cases, one might want to test multiple scenarios at once to perform Equivalence partitioning and Boundary-value analysis. A Scenario Outline provides a technique to specify multiple examples to test against a template scenario by using placeholders.[24] For example,

Scenario Outline: A user withdraws money from an ATM
    Given <Name> has a valid Credit or Debit card
    And their account balance is <OriginalBalance>
    When they insert their card
    And withdraw <WithdrawalAmount>
    Then the ATM should return <WithdrawalAmount>
    And their account balance is <NewBalance>

    Examples:
      | Name   | OriginalBalance | WithdrawalAmount | NewBalance |
      | Eric   | 100             | 45               | 55         |
      | Gaurav | 100             | 40               | 60         |
      | Ed     | 1000            | 200              | 800        |

At runtime the scenario is run against each row in the table. Column values are substituted for each of the named placeholders in the scenario.
Steps

The crux of a Scenario is defined by a sequence of Steps outlining the preconditions and flow of events that will take place. The first word of a step is a keyword, typically one of[24]

    Given - Describes the preconditions and initial state before the start of a test and allows for any pre-test setup that may occur
    When - Describes actions taken by a user during a test
    Then - Describes the outcome resulting from actions taken in the When clause

Occasionally, the combination of Given-When-Then uses other keywords to define conjunctions

    And - Logical and
    But - Logically the same as And, but used in the negative form[25]

Scenario: A user attempts to withdraw more money than they have in their account
    Given John has a valid Credit or Debit card
    And his account balance is $20
    When he inserts his card
    And withdraws $40
    Then the ATM displays an error
    And returns his card
    But his balance remains $20

Tags

Gherkin's Feature structure forces organisation. However, in cases where this default organisation is inconvenient or insufficient, Gherkin provides Tags. Tags are @-prefixed strings and can be placed before[24]

    Feature
    Scenario
    Scenario Outline
    Examples

An element can have multiple tags and inherits from parent elements.[22][24]
Cucumber
Step definitions

Steps in Gherkin's .feature files can be considered a method invocation.[26][22] Before Cucumber can execute a step it must be told, via a step definition, how that step should be performed.

Definitions are written in Ruby and conventionally filed under features/step_definitions/*_steps.rb.[22] Definitions start with the same keywords as their invocation (including Gherkin's full language support).[22] Each definition takes two arguments[22]

    Either a regular expression or string with $variables
    A block containing ruby code to execute

Example using regular expressions

Given /(.*) has a valid Credit or Debit card/ do |name|
  # Ruby code
end

Example using strings and $variables. Note that at runtime the string is converted into a regular expression, and any $variable is converted to match (.*).[22]

Given "$name has a valid Credit or Debit card" do |name|
  # Ruby code
end

Hooks

Hooks are Cucumber's way of allowing for setup to be performed prior to tests being run and teardown to be run afterwards. They are defined as executable Ruby blocks, similar to JUnit methods marked with @Before, @After annotations. Conventionally they are placed under support/, and are applied globally.[22] Three basic types of hooks exist[22]

    Before - Runs before a scenario
    After - Runs after a scenario
    Around - Assumes control and runs around a scenario

Additional hooks include[22]

    BeforeStep
    AfterStep
    AfterConfiguration - Runs after Cucumber configuration and is passed an instance of the configuration

Before, After, and Around hooks optionally take a list of tags filtering scenarios that they apply to. A list of tags in the same string is treated as OR, while individual arguments are treated as AND; tags can be optionally negated by being preceded with ~.[22]

Example of a tagged before hook

Before('@ATM') do |scenario|
  # Ruby code
end

Hooks are often used to maintain database state, typically by cleaning up prior to running a scenario. It is also possible to start and roll back a transaction using Before and After hooks, and many Cucumber extensions provide an @txn tag for such a purpose.[24]
Integrations and implementations

Non Ruby implementations of Cucumber exist for popular languages including Java, JavaScript, and Python.[24] Support also exists for integration testing frameworks. A complete list of implementations can be found on Cucumber. Cucumber has integrated testing tools working well with many Continuous Integration configurations. There are cucumber plugins for popular CI tools like Jenkins and TeamCity and also for IDEs like Eclipse and RubyMine.

Below is an example of a step definition written for Java with Cucumber-JVM.[27]

@Given("(.*) has a valid Credit or Debit card")
public void has_card(String name) {
    // Java code
}

Formatter plugins

Cucumber uses Formatter Plugins to provide output. Several common formats are provided by default, including[24]

    JSON
    HTML
    JUnit

Available formats are not standardized across different Cucumber implementations, so offerings may differ.[24] Cucumber also supports rich output formats like images and videos.
Browser automation

Cucumber does not provide built in browser automation. However, it does work well with existing programs such as Selenium and WATiR-WebDriver.[28] It does support running tests with transactions through leveraging other programs such as ActiveRecord.[29]
Cucumber command-line

Cucumber comes with a built-in command line interface that covers a comprehensive list of instructions. Like most command line tools, cucumber provides the --help option that provides a summary of arguments the command accepts.[30]

$ cucumber --help
        -r, --require LIBRARY|DIR        Require files before executing the features.
        --i18n LANG                      List keywords for in a particular language.
                                         Run with "--i18n help" to see all languages.
        -f, --format FORMAT              How to format features (Default: pretty).
        -o, --out [FILE|DIR]             Write output to a file/directory instead of
        ...

Cucumber command line can be used to quickly run defined tests. It also supports running a subset of scenarios by filtering tags.

$ cucumber --tags @tag-name

The above command helps in executing only those scenarios that have the specified @tag-name.[30] Arguments can be provided as a logical OR or AND operation of tags. Apart from tags, scenarios can be filtered on scenario names.[30]

$ cucumber --name logout

The above command will run only those scenarios that contain the word 'logout'.

It is also useful to be able to know what went wrong when a test fails. Cucumber makes it easy to catch bugs in the code with the --backtrace option.[30]

Cucumber can also be configured to ignore certain scenarios that have not been completed by marking them with the Work In Progress tag @wip. When Cucumber is passed the --wip argument, Cucumber ignores scenarios with the 


























