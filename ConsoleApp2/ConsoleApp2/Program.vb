Imports System

Module Program
    Sub ValidateLength()
        Dim password As String
        Do
            Console.WriteLine("Enter the password")
            password = Console.ReadLine
            If Len(password) < 8 Then
                Console.WriteLine("password string entered is too short.. please try again")
            Else
                Console.WriteLine("SUCCESS!! Password entered has got: " & Len(password) & " characters")
            End If
        Loop Until Len(password) >= 8


    End Sub
    Sub ValidateMark()
        Dim mark As Integer
        Console.WriteLine("Enter the score")
        mark = Console.ReadLine
        While mark < 0 Or mark > 100
            Console.WriteLine("Please enter a valid score")
            mark = Console.ReadLine
        End While
        Console.WriteLine("You have entered valid score of: " & mark)
    End Sub


    Sub Main(args As String())

        Call ValidateLength()


    End Sub
End Module
