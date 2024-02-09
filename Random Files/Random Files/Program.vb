Imports System

Module Program
    Function Hash(ByVal id As Integer) As Integer
        Dim address As Integer
        address = id Mod 10
        Return address
    End Function
    Sub Main(args As String())
        Dim returnadd, studentid, count As Integer
        Dim name As String
        count = 0
        'FileOpen(1, "student.txt", OpenMode.Random)
        'While count < 3
        '    count += 1
        '    Console.WriteLine("ID")
        '    studentid = Console.ReadLine
        '    Console.WriteLine("Name")
        '    name = Console.ReadLine
        '    returnadd = Hash(studentid)

        '    Seek(1, returnadd)
        '    FilePut(1, studentid & " " & name, returnadd)

        'End While
        'FileClose(1)

        FileOpen(1, "student.txt", OpenMode.Random)
        Console.WriteLine("Enter studentID")
        studentid = Console.ReadLine

        returnadd = Hash(studentid)
        Seek(1, returnadd)
        FileGet(1, name)
        Console.WriteLine(name)
        FileClose(1)
    End Sub
End Module
