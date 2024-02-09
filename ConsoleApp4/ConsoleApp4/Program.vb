Imports System

Module Program
    Sub Main(args As String())
        Dim lengthofname As Integer
        Dim Name As String
        Console.WriteLine("Enter Name: ")
        Name = Console.ReadLine
        lengthofname = Len(Name)
        Console.WriteLine("Name has got: " + Str(lengthofname) + "Characters")

        'Console.WriteLine("Hello World!")
    End Sub
End Module
