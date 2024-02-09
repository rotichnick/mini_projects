Imports System

Module Program
    Sub Main(args As String())
        Dim studentID As Integer
        Dim fname As String
        Dim lname As String
        FileOpen(1, "Students.txt", OpenMode.Output)
        Do
            Console.WriteLine("Enter fname")
            fname = Console.ReadLine
            Console.WriteLine("Enter last name")
            lname = Console.ReadLine
            Console.WriteLine("Enter student ID")
            studentID = Console.ReadLine
            If fname <> "#" Then
                PrintLine(1, studentID, fname, lname)
            End If
        Loop Until fname = "#"
        FileClose(1)
    End Sub
End Module
