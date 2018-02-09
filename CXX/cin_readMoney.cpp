

void Money::input(istream& ins)
{
    char one_char, decimal_point,
            digit1, digit2; //digits for the amount of cents
    long dollars;
    int cents;
    bool negative;//set to true if input is negative.

    ins >> one_char;
    if (one_char == '-')
    {
        negative = true;
        ins >> one_char; //read '$'
    }
    else
        negative = false;
    //if input is legal, then one_char == '$'

    ins >> dollars >> decimal_point >> digit1 >> digit2;

    if ( one_char != '$' || decimal_point != '.'
         || !isdigit(digit1) || !isdigit(digit2) )


    {
        cout << "Error illegal form for money input\n";
        exit(1);
    }

    cout << "one_char(char):" << one_char << endl;
    cout << "dollars(long):" << dollars << endl;
    cout << "decimal_point(char):" << decimal_point << endl;
    cout << "digit1(char):" << digit1 << endl;
    cout << "digit2(char):" << digit2 << endl;

    cents = digit_to_int(digit1)*10 + digit_to_int(digit2);

    all_cents = dollars*100 + cents;
    if (negative)
        all_cents = -all_cents;
}

/*
Enter an amount of money:    $     678 .  987
one_char(char):$
dollars(long):678
decimal_point(char):.
digit1(char):9
digit2(char):8
Your amount is $678.98
My amount is $10.09
One of us is richer.
$678.98 + $10.09 equals $689.07
*/
