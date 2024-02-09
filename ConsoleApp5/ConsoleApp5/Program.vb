Imports System
Imports System.Security.Cryptography

Module Program
    Sub Main(args As String())
        Dim RandNum, count, Guess As Integer
        Dim GuessCorrect As Boolean = False
        count = 0

        RandNum = Rnd() * 100
        While Not GuessCorect
            Console.WriteLine("Enter your guess")
            Guess = Console.ReadLine
            If Guess = RandNu Then
                GuessCorrect = True
                Console.WriteLine("Congratulations, you guessed right!")
            ElseIf Guess > RandNum Then
                Console.WriteLine("Wrong guess, choose a smaller number")
            Else
                Console.WriteLne("Wrong guess, choose a bigger number")
            End If
            count = count + 1
        End While
        Console.WriteLine("You made" & count & " Guesses")

        Console.WriteLine("Hello World!"
    End Sub
End Module
