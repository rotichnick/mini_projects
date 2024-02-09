Module Program
    Dim x, y, z As Single

    Sub Main(args As String())
        Dim MyString, lstr, rstr, mstr As String
        Dim strlen As Integer
        Const storedpassword = "Secret"
        Dim inputpassword As String
        Dim size As Integer
        Console.WriteLine("Please enter your password")
        inputpassword = Console.ReadLine
        size = Len(inputpassword)
        If size = Len(storedpassword) Then
            If (Left(inputpassword, 1) = Left(storedpassword, 1)) And
                (Right(storedpassword, 1) = Right(inputpassword, 1)) Then
                Console.WriteLine("Password entered has correct first and last letters")
            Else
                Console.WriteLine("Password entered is incorrect!")
            End If
        Else
            Console.WriteLine("Password entered is incorrect")
        End If
            MyString = "Independent School"
        strlen = Len("Independent School")
        Console.WriteLine("String length is: " & strlen)

        lstr = Left(MyString, 2)
        Console.WriteLine("The left string is: " & lstr)
        rstr = Right(MyString, 4)
        Console.WriteLine("The right string is: " & rstr)

        mstr = Mid(MyString, 5, 3)
        Console.WriteLine("The mid string is: " & mstr)




    End Sub

End Module
