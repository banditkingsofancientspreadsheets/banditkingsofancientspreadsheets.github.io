---
title: "Fast Excel with the Quick Access Toolbar"
date: 2019-08-05
tags: [excel]
excerpt: "Excel is still the lingua franca of Corporate Finance and is blazing fast for quick, ad-hoc analyses. I learned early on to use excel without a mouse, and with the Quick Access Toolbar and some macros, you can even make Excel feel like a video game!"
mathjax: "true"
---

Excel is still the lingua franca of Corporate Finance and is blazing fast for quick, ad-hoc analyses. I learned early on to use excel without a mouse, and with the Quick Access Toolbar and some macros, you can even make Excel feel like a video game!

Here's how my quick access toolbar is set up. I primarily work with pro forma Profit and Loss statements from our various business units, so my workflow is tailored for quick 5 minute analyses that gets presented to managers as a formatted PnL or data table in an email to go along with a short writeup.

1. Paste Values – I use this constantly to avoid pasting formulas
1. Format Painter
1. Center – fast formatting for column headers
1. Border Settings – fast formatting
1. Autofit Column Width
1. Autofit Row Height
1. Text to Columns – useful for cleaning data
1. Macro to custom format selected cell(s)
1. Macro to custom format all cells in the selected pivot table
1. Manage COM add-ins – my company uses a lot of excel add-ins that aren’t compatible with each other, so I need to toggle between various add-ins depending on the task at hand

The macros are there to convert the value in the cell to a specific $ format with no decimals and red parenthesis for negative values. I use this pattern constantly as a profit and loss analyst to present your analyses quickly to the executive waiting for your insights.

## Macros:
```
Sub Spends_Format()

'
' Spends_Format Macro
' Format Spends in $ format with negative values in red parentheses
'

'
    Selection.NumberFormat = "$#,##0_);[Red]($#,##0)"
End Sub
```
```
Sub Format_Pivot()
'
' Format_Pivot Macro
' Formats a column of a pivot in $
'
'
    On Error Resume Next
    Set pt = ActiveCell.PivotCell.PivotTable
    On Error GoTo 0
    If pt Is Nothing Then
        MsgBox "No PivotTable selected", vbInformation, "Oops..."
        Exit Sub
    End If
    For Each df In pt.DataFields
      df.NumberFormat = "$#,##0_);[Red]($#,##0)"
    Next df

End Sub
```
```
Sub Color_Format()
'
' Color_Format Macro
' Automatically formats the numbers to show blue if it's a constant, black if it's a formula, or green if it's a linked formula
' Keyboard Shortcut: Ctrl+Shift+C
'

Dim cell As Range, constantCells As Range, formulaCells As Range
Dim cellFormula As String
With Selection
    On Error Resume Next
        Set constantCells = .SpecialCells(xlCellTypeConstants, xlNumbers)
        Set formulaCells = .SpecialCells(xlCellTypeFormulas, 21)
    On Error GoTo 0
End With

If Not constantCells Is Nothing Then
    constantCells.Font.ThemeColor = xlThemeColorAccent1
    constantCells.Font.TintAndShade = 0
End If

If Not formulaCells Is Nothing Then
    For Each cell In formulaCells
        cellFormula = cell.Formula
        If cellFormula Like "*.xls*]*!*" Then
            cell.Font.ColorIndex = 3
        ElseIf cellFormula Like "*!*" And Not cellFormula Like "*\**" And Not cellFormula Like "*+*" And Not cellFormula Like "*-*" And Not cellFormula Like "*/*" And Not cellFormula Like "*%*" And Not cellFormula Like "*^*" And Not cellFormula Like "*>*" And Not cellFormula Like "*<*" And Not cellFormula Like "*>=*" And Not cellFormula Like "*<=*" And Not cellFormula Like "*<>*" And Not cellFormula Like "*&*" Then
            cell.Font.Color = -11489280
            cell.Font.TintAndShade = 0
        Else
            cell.Font.ColorIndex = 0
        End If
    Next cell
End If

End Sub

```
 