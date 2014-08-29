#!/usr/bin/python
# -*- coding: gbk -*-
#-------------------------------------------------------------------------------
# Name:        ģ��1
# Purpose:
#
# Author:      ZWW
#
# Created:     24/12/2013
# Copyright:   (c) ZWW 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx

class ComboBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Combo Box Example', size=(350, 300))
        panel = wx.Panel(self, -1)
        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight']

        flexSizer = wx.FlexGridSizer(4,4,6,6)
        flexSizer.AddGrowableCol(1)
        flexSizer.AddGrowableCol(3)

        #������ͨ��ʽ��comboBox, ���ܼ������룬������ı�Item
        commonLable = wx.StaticText(panel, -1, "��ͨ��ʽ")
        commonComboBox = wx.ComboBox(panel, -1, value = "zero", choices = sampleList, style = wx.CB_DROPDOWN)

        #�������ʽ��ComboBox��
        simpleLable = wx.StaticText(panel, -1, "����ʽ:")
        simpleComboBox = wx.ComboBox(panel, -1, value =  "zero", choices = sampleList, style = wx.CB_SIMPLE)

        #����ֻ����ʽ��ComboBox��
        readonlyLable = wx.StaticText(panel, -1, "ֻ����ʽ:")
        readonlyComboBox = wx.ComboBox(panel, -1, value =  "zero", choices = sampleList, style = wx.CB_READONLY)

        #����������������б�
        cityDict = {'����':["�Ϸ�", "����"], "����":["����","�Ͼ�"]}

        #�����һ���˵�
        proviceLable = wx.StaticText(panel, -1, "ʡ��:")
        proviceComboBox = wx.ComboBox(panel, -1, value =  cityDict.keys()[0], choices = cityDict.keys(), style = wx.CB_READONLY)
        #����ڶ����˵�
        cityLable = wx.StaticText(panel, -1, "����:")
        cityComboBox = wx.ComboBox(panel, -1, value =  cityDict[cityDict.keys()[0]][0], choices = cityDict[cityDict.keys()[0]], style = wx.CB_READONLY)

        flexSizer.AddMany([
                            (commonLable, 0, wx.SHAPED|wx.ALIGN_RIGHT), (commonComboBox, 1, wx.EXPAND), (simpleLable, 0, wx.SHAPED|wx.ALIGN_RIGHT),(simpleComboBox, 1, wx.EXPAND)
                            ,(readonlyLable, 0, wx.SHAPED|wx.ALIGN_RIGHT), (readonlyComboBox, 1, wx.EXPAND),(wx.Size(6,6), 0, wx.SHAPED|wx.ALIGN_RIGHT), (wx.Size(6,6), 1, wx.EXPAND)
                            ,(proviceLable, 0, wx.SHAPED|wx.ALIGN_RIGHT), (proviceComboBox, 1, wx.EXPAND),(wx.Size(6,6), 0, wx.SHAPED|wx.ALIGN_RIGHT), (wx.Size(6,6), 1, wx.EXPAND)
                            ,(cityLable, 0, wx.SHAPED|wx.ALIGN_RIGHT), (cityComboBox, 1, wx.EXPAND),(wx.Size(6,6), 0, wx.SHAPED|wx.ALIGN_RIGHT), (wx.Size(6,6), 1, wx.EXPAND)
                            ])

        panel.SetSizerAndFit(flexSizer)


        #���� һ�������б��л�ʱ��ˢ�¶����˵������Ӧ�¼�
        self.__ProvinceComboBox = proviceComboBox
        self.__SecityDict = cityDict
        self.__CityComboBox= cityComboBox
        panel.Bind(wx.EVT_COMBOBOX,  self.__OnComboBoxSelected, proviceComboBox,)

    def __OnComboBoxSelected(self, event):
        currentProvinceIndex = self.__ProvinceComboBox.GetSelection()
        if wx.NOT_FOUND == currentProvinceIndex: return
        value = self.__ProvinceComboBox.GetItems()[currentProvinceIndex]

        #ע��������List dict �ȴ洢ʱ��, utf-8 ��ʽ��һ������
        value = value.encode('utf-8')

        cityList = self.__SecityDict[value]
        self.__CityComboBox.SetItems(cityList)
        self.__CityComboBox.SetValue(cityList[0])




def main():
    app = wx.PySimpleApp()
    ComboBoxFrame().Show()
    app.MainLoop()


if __name__ == '__main__':
    main()