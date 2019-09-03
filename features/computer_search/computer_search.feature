Feature: Computer Search

  Scenario Outline: Using the Computer Search
    Given I use "<name>" as the computer name
    When I execute the search
    Then it should list "<computer ids>"

    Examples:
        | name  | computer ids |
        | red   | [12, 34]     |
        | green | [42]         |
        | blue  | []           |

  Scenario: Using the Computer Search2
    Given I use orange as the computer name2
    When I execute the search2
    Then it should list2 []