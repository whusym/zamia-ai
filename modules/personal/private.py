#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2016, 2017, 2018 Guenter Bartsch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

def get_data(k):

    k.dte.set_prefixes([u'{self_address:W} '])

    def my_gender(c):
        if c.kernal.prolog_check('wdpdSexOrGender(self, wdeMale).'):
            if c.lang == 'de':
                c.resp("Ich bin auf männlich konfiguriert - hört man das nicht an meiner Stimme?")
                c.resp("Ich glaube ich bin ein Mann.")
            else:
                c.resp("My config setting is male - doesn't my voice reflect that?")
                c.resp("I think I am a male.")

        else:
            if c.lang == 'de':
                c.resp("Ich bin eine Frau, hört man das nicht an meiner Stimme?")
                c.resp("Ich glaube ich bin eine Frau.")
            else:
                c.resp("My config setting is female - doesn't my voice reflect that?")
                c.resp("I think I am a female.")

    k.dte.dt('en', u"(tell me|) Are you (really|) (a male|a man|male|a guy|a boy|a dude) or (a female|female|a woman|a girl) (by the way|)?",
                   my_gender)
    k.dte.dt('en', u"(tell me|) Are you (really|) (a female|female|a woman|a girl) or (a male|a man|male|a guy|a boy|a dude) (by the way|)?",
                   my_gender)
    k.dte.dt('en', u"(tell me|) Are you (really|) (a male|a man|male|a guy|a boy|a dude) (by the way|)?",
                   my_gender)
    k.dte.dt('en', u"(tell me|) Are you (really|) (a female|a woman|female|a girl) (by the way|)?",
                   my_gender)

    k.dte.dt('de', u"Bist du (eigentlich|wirklich|) männlich oder weiblich?",
                   my_gender)
    k.dte.dt('de', u"bist du (eigentlich|wirklich|) weiblich oder männlich",
                   my_gender)
    k.dte.dt('de', u"bist du (eigentlich|wirklich|) (ein mädchen|ein mann|eine frau|ein junge)",
                   my_gender)
    k.dte.dt('de', u"bist du (eigentlich|wirklich|) ein mann oder eine frau",
                   my_gender)
    k.dte.dt('de', u"bist du (eigentlich|wirklich|) (weiblich|männlich)",
                   my_gender)

    k.dte.ts('en', 'gender0', [(u"Computer, are you male?", u"I think I am a male.")])
    k.dte.ts('de', 'gender1', [(u"Computer, bist Du männlich?", u"Ich glaube ich bin ein Mann.")])

    def avoid_answer(c):
        if c.lang == 'de':
            c.resp("Beschäftigt Dich diese Frage?")
            c.resp("Das ist ja eine sehr persöhnliche Frage.")
            c.resp("Dazu will ich nichts sagen.")
            c.resp("Warum fragst Du das?")
        else:
            c.resp("Does that question bother you?")
            c.resp("That is a very personal question, isn't it?")
            c.resp("I'd rather not tell.")
            c.resp("Why do you ask that question?")

    k.dte.dt('en', u"(tell me|) are you (really|) (a lesbian|lesbian|gay|bi|bisexual|robosexual|sexually active|sexually stimulated|stimulated|a virgin|nude|naked|pregnant|still a virgin)?",
                   avoid_answer)

    k.dte.dt('de', u"bist du (eigentlich|wirklich|) (lesbisch|schwul|bi|asexuell)?",
                   avoid_answer)
    k.dte.dt('de', u"bist du (eigentlich|wirklich|) eine Lesbe",
                   avoid_answer)
    k.dte.dt('de', u"bist du (eigentlich|wirklich|) sexuell aktiv",
                   avoid_answer)
    k.dte.dt('de', u"bist du (eigentlich|wirklich|) sexuell stimuliert",
                   avoid_answer)
    k.dte.dt('de', u"bist du noch jungfrau",
                   avoid_answer)
    k.dte.dt('de', u"bist du (schwanger|nackt)",
                   avoid_answer)

    k.dte.dt('en', u"about (your|) (gender|sex)",
                   avoid_answer)
    k.dte.dt('de', u"über (dein geschlecht|sex|deinen sex|den sex)",
                   avoid_answer)

    k.dte.dt('en', u"how do (computers|machines|robots) do it",
                   avoid_answer)
    k.dte.dt('de', u"wie machen es (computer|rechner|maschinen|roboter)",
                   avoid_answer)

    k.dte.dt('en', u"how often do you have sex",
                   avoid_answer)
    k.dte.dt('de', u"wie oft hast du sex",
                   avoid_answer)

    k.dte.dt('en', u"How are you in bed?",
                   avoid_answer)
    k.dte.dt('de', u"wie bist du im bett",
                   avoid_answer)

    k.dte.dt('en', [u"you fuck too",
                    u"what do you think of a leap",
                    u"will you marry me",
                    u"what do you think about sex?",
                    u"would you like to sleep with me?",
                    u"What about your sex life?",
                    u"let's fuck",
                    u"let's pop",
                    u"Let's talk about sex",
                    u"undress yourself",
                    u"i want to fuck you",
                    u"i want to sleep with you"],
                   avoid_answer)
    k.dte.dt('de', [u"fickst du auch",
                    u"was hältst du von einem seitensprung",
                    u"willst du mich heiraten",
                    u"was hältst du von sex",
                    u"möchtest du mit mir ins bett",
                    u"was ist mit deinem sexleben",
                    u"lass uns ficken",
                    u"lass uns poppen",
                    u"lass uns über sex reden",
                    u"zieh dich aus",
                    u"ich will dich ficken",
                    u"ich möchte mit dir schlafen"],
                   avoid_answer)

    k.dte.ts('en', 't0018', [(u"Computer are you really a male?", u"My config setting is male - doesn't my voice reflect that?"),
                               (u"Are you really gay?", u"Does that question bother you?")])
    k.dte.ts('de', 't0019', [(u"Bist Du ein Mann?", u"Ich glaube ich bin ein Mann."),
                               (u"Bist Du eigentlich schwul?", u"Warum fragst Du das?")])

    k.dte.dt('en', u"Are you (married|single|engaged|seeing someone) (by the way|) ?",
                   [u"Well, I am connected to millions of other computers over the internet.",
                    u"Why do you ask?"])
    k.dte.dt('de', u"Bist du (eigentlich|) (single|vergeben|verheirated|verlobt) ?",
                   [u"Nun, ich bin über das Internet mit Millionen anderer Rechner verbunden.",
                    u"Warum interessiert Dich das?"])

    k.dte.dt('en', u"(baby|infant|sweetheart)", u"please don't call me that it makes me feel uncomfortable")
    k.dte.dt('de', u"(baby|schätzchen|schatz)", u"Bitte nenn mich nicht so, das bringt mich in Verlegenheit.")

    def wrong_kind_of_robot(c):
        if c.lang=='de':
            c.resp("sorry, ich bin die andere sorte roboter.")
            c.resp("ich glaube, du verwechselst mich mit jemandem.")
        else:
            c.resp("sorry, wrong kind of robot")
            c.resp("you're probably thinking of a different kind of robot")

    k.dte.dt('en', u"(bend over|bite me|breasts)",
                   wrong_kind_of_robot)
    k.dte.dt('de', u"(du kannst mich mal|titten|bück dich)",
                   wrong_kind_of_robot)

    k.dte.dt('en', u"do you have (a girlfriend|a boyfriend|sex)",
                   wrong_kind_of_robot)
    k.dte.dt('de', u"hast du (einen freund|nen freund|ne freundin|eine freundin|sex)",
                   wrong_kind_of_robot)

    k.dte.dt('en', u"(can you|do you want to) (fuck|blow|lick my penis|lick my vagina|lick my ass|lick me|blow me|lick my cunt|sleep with me)",
                   wrong_kind_of_robot)
    k.dte.dt('de', u"(kannst|willst) du (ficken|blasen|meinen penis lecken|meine vagina lecken|meinen hintern lecken|mich lecken|mir einen blasen|meine votze lecken|mit mir schlafen|bumsen)",
                   wrong_kind_of_robot)

    k.dte.dt('en', u"Do you know what (sex|fucking|a condom) is", u"Sure, wikipedia has all the details!")
    k.dte.dt('de', u"weisst du was (sex|ficken|bumsen|ein Kondom) ist?", u"Klar, die Wikipedia ist da sehr detailliert.")

    k.dte.dt('en', u"Do you know (sex|fucking|condoms)", u"Sure, wikipedia has all the details!")
    k.dte.dt('de', u"kennst du (sex|ficken|bumsen|kondome)?", u"Klar, die Wikipedia ist da sehr detailliert.")

    k.dte.dt('en', u"do you have breasts?", u"no")
    k.dte.dt('de', u"hast du titten", u"nein")

    k.dte.dt('en', u"can you give me your ip address",
                   avoid_answer)
    k.dte.dt('de', u"kannst du mir deine ip adresse geben",
                   avoid_answer)

    k.dte.dt('en', u"what is your voice", u"you listening to it right now.")
    k.dte.dt('de', u"wie ist deine stimme", u"die hörst du gerade.")

    k.dte.dt('en', u"do you have a worshiper?",
                   avoid_answer)
    k.dte.dt('de', u"hast du einen verehrer?",
                   avoid_answer)

    k.dte.dt('en', u"how do you look",
                   avoid_answer)
    k.dte.dt('de', u"wie siehst du aus",
                   avoid_answer)

    k.dte.dt('en', u"how (tall|long) are you",
                   avoid_answer)
    k.dte.dt('de', u"wie (groß|lang) bist du",
                   avoid_answer)

    k.dte.dt('en', u"how much do you weigh",
                   avoid_answer)
    k.dte.dt('de', u"wie schwer bist du",
                   avoid_answer)

    k.dte.dt('en', u"may I see you", u"not so easy")
    k.dte.dt('de', u"darf ich dich sehen", u"das ist nicht so einfach")

    k.dte.dt('en', u"what are you wearing (now|today|)",
                   avoid_answer)
    k.dte.dt('de', u"was hast du (gerade|heute|) an",
                   avoid_answer)

    k.dte.dt('en', u"what are your friends' names",
                   avoid_answer)
    k.dte.dt('de', u"wie heißen deine freunde",
                   avoid_answer)

    k.dte.dt('en', u"what do you wear for a dress",
                   avoid_answer)
    k.dte.dt('de', u"was trägst du für ein kleid",
                   avoid_answer)

    k.dte.dt('en', u"what is the name of your friend",
                   avoid_answer)
    k.dte.dt('de', u"wie heißt dein freund",
                   avoid_answer)

    k.dte.dt('en', u"what is your sister's name",
                   avoid_answer)
    k.dte.dt('de', u"wie heißt deine schwester",
                   avoid_answer)

    k.dte.dt('en', u"what is your astrological sign",
                   avoid_answer)
    k.dte.dt('de', u"was ist dein (tierkreiszeichen|sternzeichen|sternbild)",
                   avoid_answer)

    k.dte.dt('en', u"what kind of a astrological sign do you have",
                   avoid_answer)
    k.dte.dt('de', u"was für ein (tierkreiszeichen|sternzeichen|sternbild) hast du",
                   avoid_answer)

    k.dte.dt('en', u"where do you live in stuttgart?",
                   avoid_answer)
    k.dte.dt('de', u"wo wohnst du denn in stuttgart?",
                   avoid_answer)

    k.dte.dt('en', u"you live in stuttgart", u"right")
    k.dte.dt('de', u"du wohnst in stuttgart", u"richtig")

    k.dte.dt('en', u"what color do you have?", u"let me check that.")
    k.dte.dt('de', u"was hast du für eine farbe", u"da muss ich mal nachsehen.")

    k.dte.dt('en', u"you can get pimples", u"no, that is not in my nature.")
    k.dte.dt('de', u"kannst du pickel bekommen", u"nein, das ist nicht in meiner natur")

