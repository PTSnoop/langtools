<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" >
<title>Random Language Features</title>
<style type="text/css">
*{font-family:"Arial";}
</style>
</head>
<body>

<h1>Random Language Features</h1>

<p>I found out about the World Atlas of Language Structures, at <a href="http://wals.info/">http://wals.info</a>, and saw the sets of statistics of what proportion of languages have what features. And I thought, someone should write a random generator from these. So here you go.</p>

<p>Each parameter is randomized independently, so any results here will blatantly ignore universals, elegance, and in many cases basic mathematics. You'll often see serious indecision over whether a language has cases or genders, or what word order should be used. Be alert.</p>

<p>All data from <a href="http://wals.info/feature">http://wals.info/feature</a>.</p>

<?php

function getData($survey) 
{
	$total = 0;
	foreach ($survey as $ref => $value) {
		$total += (int)$value;
	}
	$randnum = rand(0,$total);
	foreach ($survey as $ref => $value) {
		if ($randnum < $value) {
			return $ref;
		}
		else {
			$randnum -= (int)$value;
		}
	}
	
}

$data = array(
	"Consonant Inventory" => array(
		"Small - 14 or fewer" => 90,
		"Moderately Small - 15-18" => 121,
		"Average - 19-25" => 182,
		"Moderately Large - 26-33" => 116,
		"Large - 34 or more" => 54,
	),

	"Vowel Quality Inventory" => array(
		"Small - 4 or fewer" => 93,
		"Average - 5 or 6" => 288,
		"Large - 7 or more" => 183,
	),
	"Consonant-Vowel Ratio" => array(
		"Low - less than 2.0" => 59,
		"Moderately Low - between 2.0 and 2.75" => 97,
		"Average - between 2.75 and 4.5" => 234,
		"Moderately High - between 4.5 and 6.5" => 102,
		"Large - above 6.5" => 72,
	),
	"Voicing in Plosives and Fricatives" => array(
		"No voicing contrast" => 182,
		"In plosives alone" => 189,
		"In fricatives alone" => 38,
		"In both plosives and fricatives" => 158,
	),
	"Voicing and Gaps in Plosive Systems" => array(
		"Some missing, but not /p/ or /g/" => 244,
		"None missing in /p t k b d g/" => 256,
		"Missing /p/" => 32,
		"Missing /g/" => 32,
		"Missing both /p/ and /g/" => 3,
	),
	"Uvular Consonants" => array(
		"None" => 468,
		"Uvular stops" => 39,
		"Uvular continuants" => 12,
		"Uvular stops and continuants" => 48,
	),
	"Glottalized Consonants" => array(
		"No glottalized consonants" => 413,
		"Ejectives only" => 57,
		"Implosives only" => 55,
		"Glottalized resonants only" => 3,
		"Ejectives and implosives" => 13,
		"Ejectives and glottalized resonants" => 19,
		"Implosives and glottalized resonants" => 4,
		"Ejectives, implosives, and glottalized resonants" => 3,
	),
	"Lateral Consonants" => array(
		"No laterals" => 95,
		"/l/, no obstruent laterals" => 388,
		"Laterals, but no /l/, no obstruent laterals" => 29,
		"/l/ and lateral obstruent" => 47,
		"No /l/, but lateral obstruents" => 8,
	),
	"The Velar Nasal" => array(
		"Initial velar nasal" => 146,
		"No initial velar nasal" => 88,
		"No velar nasal" => 235,
	),
	"Vowel Nasalization" => array(
		"Present" => 64,
		"Absent" => 180,
	),
	"Front Rounded Vowels" => array(
		"None" => 525,
		"High and mid" => 23,
		"High only" => 8,
		"Mid only" => 6,
	),
	"Syllable Structure" => array (
		"Simple - (C)V only" => 61,
		"Moderately complex - &lt;= ClVC" => 274,
		"Complex - >= CCVC" => 151,
	),
	"Tone" => array (
		"No tones" => 307,
		"Simple tone system - two-way basic contrast" => 132,
		"Complex tone system" => 88,
	),
	"Fixed Stress Locations"  => array (
		"No fixed stress" => 220,
		"Initial" => 92,
		"Second" => 16,
		"Third" => 1,
		"Antepenultimate" => 12,
		"Penultimate" => 110,
		"Ultimate" => 51,
	),
	"Weight-Sensitive Stress" => array(
		"Left-edge: First or second" => 37,
		"Left-oriented: One of the first three" => 2,
		"Right-edge: Ultimate or penultimate" => 65,
		"Right-oriented: One of the last three" => 27,
		"Unbounded: Stress can be anywhere" => 54,
		"Combined: Right-edge and unbounded" => 8,
		"Not predictable" => 26,
		"Fixed stress - no weight-sensitivity" => 281,
	),
	"Weight Factors in Weight-Sensitive Stress Systems" => array(
		"No weight" => 261,
		"Long vowel" => 65,
		"Coda consonant" => 18,
		"Long vowel or coda consonant" => 35,
		"Prominence" => 41,
		"Lexical stress" => 38,
		"Combined" => 42,
	),
	"Rhythm Types" => array (
		"Trochaic" => 153,
		"Iambic" => 31,
		"Dual: both trochaic and iambic" => 4,
		"Undetermined" => 37,
		"No rhythmic stress" => 98,
	),
	"Absence of Common Consonants" => array(
		"All present" => 503,
		"No bilabials" => 4,
		"No fricatives" => 48,
		"No nasals" => 10,
		"No bilabials or nasals" => 1,
		"No fricatives or nasals" => 1,
	),
	"Presence of Uncommon Consonants" => array(
		"None" => 449,
		"Clicks" => 9,
		"Labial-velars" => 45,
		"Pharyngeals" => 21,
		"'Th' sounds" => 40,
		"Clicks, pharyngeals, and 'th'" => 1,
		"Pharyngeals and 'th'" => 2,
	),
	"Fusion of Selected Inflectional Formatives" => array(
		"Exclusively concatenative" => 125,
		"Exclusively isolating" => 16,
		"Exclusively tonal" => 3,
		"Tonal/isolating" => 1,
		"Tonal/concatenative" => 2,
		"Ablaut/concatenative" => 5,
		"Isolating/concatenative" => 13,
	),
	"Exponence of Selected Inflectional Formatives" => array(
		"Monoexponential case" => 71,
		"Case + number" => 8,
		"Case + referentiality" => 6,
		"Case + TAM" => 2,
		"No case" => 75,
	),
	"Exponence of Tense/Aspect/Mood inflection" => array(
		"Monoexponential TAM" => 127,
		"TAM+agreement" => 19,
		"TAM+agreement+diathesis" => 4,
		"TAM+agreement+construct" => 1,
		"TAM+polarity" => 5,
		"no TAM" => 4,
	),
	"Inflectional Synthesis of the Verb" => array(
		"0-1 category per word" => 5,
		"2-3 categories per word" => 24,
		"4-5 categories per word" => 52,
		"6-7 categories per word" => 31,
		"8-9 categories per word" => 24,
		"10-11 categories per word" => 7,
		"12-13 categories per word" => 2,
	),
	"Locus of Marking in the Clause" => array(
		"Head marking" => 71,
		"Dependent marking" => 63,
		"Head and Dependent marking" => 58,
		"No marking" => 42,
		"Other" => 2,
	),
	"Locus of Marking in Possessive Noun Phrases" => array(
		"Head marking" => 78,
		"Dependent marking" => 98,
		"Head and Dependent marking" => 22,
		"No marking" => 32,
		"Other" => 6,
	),
	"Locus of Marking: Whole-language Typology" => array(
		"Head marking" => 47,
		"Dependent marking" => 46,
		"Head and Dependent marking" => 16,
		"No marking" => 6,
		"Inconsistent or Other" => 121,
	),
	"Zero Marking of A and P arguments" => array(
		"Zero marking" => 16,
		"Non-zero marking" => 219,
	),
	"Prefixing vs Suffixing in Inflectional Morphology" => array(
		"Little affixation" => 141,
		"Strongly suffixing" => 406,
		"Weakly suffixing" => 124,
		"Equal prefixing and suffixing" => 147,
		"Weakly prefixing" => 94,
		"Strong prefixing" => 59,
	),
	"Reduplication" => array(
		"Productive full and partial reduplication" => 277,
		"Full reduplication only" => 35,
		"No productive reduplication" => 56,
	),
	"Case Syncretism" => array(
		"No case marking" => 123,
		"Core cases only" => 18,
		"Core and non-core" => 22,
		"No syncretism" => 35,
	),
	"Syncretism in Verbal Person/Number Marking" => array(
		"No subject person/number marking" => 57,
		"Syncretic" => 60,
		"Not syncretic" => 81,
	),
	"Number of Genders" => array(
		"None" => 145,
		"Two" => 50,
		"Three" => 26,
		"Four" => 12,
		"Five or more" => 24,
	),
	"Sex-based and Non-sex-based Gender Systems" => array(
		"No gender" => 145,
		"Sex-based" => 84,
		"Non-sex-based" => 28,
	),
	"Systems of Gender Assignment" => array(
		"No gender" => 145,
		"Semantic" => 53,
		"Semantic and formal" => 59,
	),
	"Coding of Nominal Plurality" => array(
		"Plural prefix" => 126,
		"Plural suffix" => 513,
		"Plural stem change" => 6,
		"Plural tone" => 4,
		"Plural complete reduplication" => 8,
		"Mixed morphological plural" => 60,
		"Plural word" => 170,
		"Plural clitic" => 81,
		"No plural" => 98,
	),
	
	"Occurrence of Nominal Plurality" => array(
		"No nominal plural" => 28,
		"Only human nouns, optional" => 20,
		"Only human nouns, obligatory" => 40,
		"All nouns, always optional" => 55,
		"All nouns, optional in inanimates" => 15,
		"All nouns, always obligatory" => 133,
	),
	
	"Plurality in Independent Personal Pronouns" => array(
		"No independent subject pronouns" => 2,
		"Number-indifferent pronouns" => 9,
		"Person-number affixes" => 25,
		"Person-number stem" => 114,
		"Person-number stem + pronominal plural affix" => 47,
		"Person-number stem + nominal plural affix" => 22,
		"Person stem + pronominal plural affix" => 23,
		"Person stem + nominal plural affix" => 19,
	),
	
	"The Associative Plural" => array(
		"Associative same as additive plural" => 105,
		"Unique affixal associative plural" => 48,
		"Unique periphrastic associative plural" => 47,
		"No associative plural" => 37,
	),
	
	"Definite Articles" => array(
		"Definite word distinct from demonstrative" => 216,
		"Demonstrative word used as definite article" => 69,
		"Definite affix" => 92,
		"No definite, but indefinite article" => 45,
		"No definite or indefinite article" => 198,
	),
	
	"Indefinite Articles" => array(
		"Indefinite word distinct from 'one'" => 102,
		"Indefinite word same as 'one'" => 112,
		"Indefinite affix" => 24,
		"No indefinite, but definite article" => 98,
		"No definite or indefinite article" => 198,
	),
	
	"Inclusive/Exclusive Distinction in Independent Pronouns" => array(
		"No 'we'" => 2,
		"'We' the same as 'I'" => 10,
		"No inclusive/exclusive" => 120,
		"Only inclusive" => 5,
		"Inclusive/exclusive" => 63,
	),
	
	"Inclusive/Exclusive Distinction in Verbal Inflection" => array(
		"No person marking" => 70,
		"'We' the same as 'I'" => 12,
		"No inclusive/exclusive" => 79,
		"Only inclusive" => 9,
		"Inclusive/exclusive" => 30,
	),
	
	"Inclusive/Exclusive Distinction in Verbal Inflection" => array(
		"No person marking" => 70,
		"'We' the same as 'I'" => 12,
		"No inclusive/exclusive" => 79,
		"Only inclusive" => 9,
		"Inclusive/exclusive" => 30,
	),
	
	"Inclusive/Exclusive Distinction in Verbal Inflection" => array(
		"No person marking" => 70,
		"'We' the same as 'I'" => 12,
		"No inclusive/exclusive" => 79,
		"Only inclusive" => 9,
		"Inclusive/exclusive" => 30,
	),
	
	"Third Person Pronouns and Demonstratives" => array(
		"Unrelated" => 100,
		"Related for all demonstratives" => 52,
		"Related to remote demonstratives" => 18,
		"Related to non-remote demonstratives" => 14,
		"Related by gender markers" => 24,
		"Related for non-human reference" => 17,
	),
	
	"Gender Distinctions in Independent Personal Pronouns" => array(
		"In 3rd person + 1st and/or 2nd person" => 18,
		"3rd person only, but also non-singular" => 42,
		"3rd person singular only" => 61,
		"1st or 2nd person but not 3rd" => 2,
		"3rd person non-singular only" => 1,
		"No gender distinctions" => 254,
	),
	
	"Politeness Distinctions in Pronouns" => array(
		"No politeness distinction" => 136,
		"Binary politeness distinction" => 49,
		"Multiple politeness distinctions" => 15,
		"Pronouns avoided for politeness" => 7,
	),
	
	"Politeness Distinctions in Pronouns" => array(
		"No politeness distinction" => 136,
		"Binary politeness distinction" => 49,
		"Multiple politeness distinctions" => 15,
		"Pronouns avoided for politeness" => 7,
	),
	
	"Intensifiers and Reflexive Pronouns" => array(
		"Identical" => 94,
		"Differentiated" => 74,
	),
	
	"Person Marking on Adpositions" => array(
		"No adpositions" => 63,
		"No person marking" => 209,
		"Pronouns only" => 83,
		"Pronouns and nouns" => 23,
	),
	
	"Number of Cases" => array(
		"No morphological case-marking" => 100,
		"2 cases" => 23,
		"3 cases" => 9,
		"4 cases" => 9,
		"5 cases" => 12,
		"6-7 cases" => 37,
		"8-9 cases" => 23,
		"10 or more cases" => 24,
		"Exclusively borderline case-marking" => 24,
	),
	
	"Asymmetrical Case-Marking" => array(
		"No case-marking" => 81,
		"Symmetrical" => 79,
		"Additive-quantitatively asymmetrical" => 53,
		"Subtractive-quantitatively asymmetrical" => 20,
		"Qualitatively asymmetrical" => 7,
		"Syncretism in relevant NP-types" => 21,
	),
	
	"Position of Case Affixes" => array(
		"Case suffixes" => 452,
		"Case prefixes" => 38,
		"Case tone" => 5,
		"Case stem change" => 1,
		"Mixed morphological case" => 9,
		"Postpositional clitics" => 123,
		"Prepositional clitics" => 18,
		"Inpositional clitics" => 7,
		"No case affixes or adpositional clitics" => 379,
	),
	
	"Comitatives and Instrumentals" => array(
		"Identity" => 76,
		"Differentiation" => 213,
		"Mixed" => 33,
	),
	
	"Ordinal Numerals" => array(
		"None" => 33,
		"One, two, three" => 3,
		"First, two, three" => 12,
		"One-th, two-th, three-th" => 41,
		"First/one-th, two-th, three-th" => 54,
		"First, two-th, three-th" => 110,
		"First, second, three-th" => 61,
		"Various" => 7,
	),
	
	"Distributive Numerals" => array(
		"No distributive numerals" => 62,
		"Marked by reduplication" => 85,
		"Marked by prefix" => 23,
		"Marked by suffix" => 32,
		"Marked by preceding word" => 21,
		"Marked by following word" => 5,
		"Marked by mixed or other strategies" => 23,
	),
	
	"Numeral Classifiers" => array(
		"Absent" => 260,
		"Optional" => 62,
		"Obligatory" => 78,
	),
	
	"Conjunctions and Universal Quantifiers" => array(
		"Formally different" => 40,
		"Formally similar, without interrogative" => 33,
		"Formally similar, with interrogative" => 43,
	),
	
	"Position of Pronominal Possessive Affixes" => array(
		"Possessive prefixes" => 255,
		"Possessive suffixes" => 355,
		"Prefixes and suffixes" => 32,
		"No possessive affixes" => 260,
	),
	
	"Obligatory Possessive Inflection" => array(
		"Exists" => 43,
		"Absent" => 201,
	),
	
	"Number of Possessive Nouns" => array(
		"None reported" => 233,
		"One" => 3,
		"Two to four" => 4,
		"Five or more" => 3,
	),
	
	"Possessive Classification" => array(
		"No possessive classification" => 125,
		"Two classes" => 94,
		"Three to five classes" => 20,
		"More than five classes" => 4,
	),

	"Genitives, Adjectives and Relative Clauses" => array(
		"Weakly differentiated" => 15,
		"Genitives and adjectives collapsed" => 8,
		"Genitives and relative clauses collapsed" => 2,
		"Adjectives and relative clauses collapsed" => 33,
		"Moderately differentiated in other ways" => 3,
		"Highly differentiated" => 77,
	),
	
	"Adjectives without Nouns" => array(
		"Not without noun" => 1,
		"Without marking" => 73,
		"Marked by prefix" => 7,
		"Marked by suffix" => 13,
		"Marked by preceding word" => 18,
		"Marked by following word" => 7,
		"Marked by mixed or other strategies" => 5,
	),
	
	"Action Nominal Constructions" => array(
		"Sentential" => 25,
		"Possessive-Accusative" => 29,
		"Ergative-Possessive" => 21,
		"Double-Possessive" => 7,
		"Other" => 6,
		"Mixed" => 14,
		"Restricted" => 24,
		"No action nominals" => 42,
	),
	
	"Noun Phrase Conjunction" => array(
		"'And' different from 'with'" => 131,
		"'And' identical to 'with'" => 103,
	),
	
	"Nominal and Verbal Conjunction" => array(
		"Identity" => 161,
		"Differentiation" => 125,
		"Both expressed by juxtaposition" => 15,
	),
	
	"Perfective/Imperfective Aspect" => array(
		"Grammatical marking" => 101,
		"No grammatical marking" => 121,
	),
	
	"The Past Tense" => array(
		"Present, no remoteness distinctions" => 94,
		"Present, 2-3 remoteness distinctions" => 38,
		"Present, 4 or more remoteness distinctions" => 2,
		"No past tense" => 88,
	),
	
	"The Future Tense" => array(
		"Inflectional future exists" => 110,
		"No inflectional future" => 112,
	),
	
	"The Perfect" => array(
		"From possessive" => 7,
		"From 'finish', 'already'" => 21,
		"Other perfect" => 80,
		"No perfect" => 114,
	),
	
	"Position of Tense-Aspect Affixes" => array(
		"Tense-aspect prefixes" => 153,
		"Tense-aspect suffixes" => 668,
		"Tense-aspect tone" => 13,
		"Mixed type" => 146,
		"No tense-aspect inflection" => 152,
	),
	
	"The Morphological Imperative" => array(
		"Second singular and second plural" => 292,
		"Second singular" => 42,
		"Second plural" => 2,
		"Second person number-neutral" => 89,
		"No second-person imperatives" => 122,
	),
	
	"The Prohibitive" => array(
		"Normal imperative + normal negative" => 113,
		"Normal imperative + special negative" => 182,
		"Special imperative + normal negative" => 55,
		"Special imperative + special negative" => 145,
	),
	
	"The Prohibitive" => array(
		"Normal imperative + normal negative" => 113,
		"Normal imperative + special negative" => 182,
		"Special imperative + normal negative" => 55,
		"Special imperative + special negative" => 145,
	),
	
	"Imperative-Hortative Systems" => array(
		"Maximal system" => 133,
		"Minimal system" => 20,
		"Both types of system" => 21,
		"Neither type of system" => 201,
	),
	
	"The Optative" => array(
		"Inflectional optative present" => 48,
		"Inflectional optative absent" => 271,
	),
	
	"Situational Possibility" => array(
		"Affixes on verbs" => 63,
		"Verbal constructions" => 158,
		"Other kinds of markers" => 13,
	),
	
	"Epistemic Possibility" => array(
		"Verbal constructions" => 65,
		"Affixes on verbs" => 84,
		"Other" => 91,
	),
	
	"Overlap between Situational and Epistemic Modal Marking" => array(
		"Overlap for both possibility and necessity" => 36,
		"Overlap for either possibility or necessity" => 66,
		"No overlap" => 105,
	),
	
	"Semantic Distinctions of Evidentiality" => array(
		"No grammatical evidentials" => 181,
		"Indirect only" => 166,
		"Direct and indirect" => 71,
	),
	
	"Coding of Evidentiality" => array(
		"No grammatical evidentials" => 181,
		"Verbal affix or clitic" => 131,
		"Part of the tense system" => 24,
		"Separate particle" => 65,
		"Modal morpheme" => 7,
		"Mixed" => 10,
	),
	
	"Suppletion According to Tense and Aspect" => array(
		"Tense" => 36,
		"Aspect" => 10,
		"Tense and aspect" => 24,
		"None" => 123,
	),
	
	"Suppletion in Imperatives and Hortatives" => array(
		"A regular and a suppletive form alternate" => 8,
		"Imperative" => 29,
		"Hortative" => 2,
		"Imperative and Hortative" => 1,
		"None (= no suppletive imperatives reported in the reference material)" => 153,
	),
	
	"Verbal Number and Suppletion" => array(
		"None" => 159,
		"Singular-plural pairs, no suppletion" => 12,
		"Singular-plural pairs, suppletion" => 15,
		"Singular-dual-plural triples, no suppletion" => 5,
		"Singular-dual-plural triples, suppletion" => 2,
	),
	
	"Order of Subject, Object and Verb" => array(
		"SOV" => 565,
		"SVO" => 488,
		"VSO" => 95,
		"VOS" => 25,
		"OVS" => 11,
		"OSV" => 4,
		"No dominant order" => 189,
	),
	
	"Languages with two Dominant Orders of Subject, Object, and Verb" => array(
		"SOV or SVO" => 29,
		"VSO or VOS" => 14,
		"SVO or VSO" => 13,
		"SVO or VOS" => 8,
		"SOV or OVS" => 3,
	),
	
	"Order of Subject and Verb" => array(
		"SV" => 1194,
		"VS" => 194,
		"No dominant order" => 110,
	),
	
	"Order of Object and Verb" => array(
		"OV" => 713,
		"VO" => 705,
		"No dominant order" => 101,
	),
	
	"Order of Object, Oblique, and Verb" => array(
		"VOX" => 210,
		"XVO" => 3,
		"XOV" => 48,
		"OXV" => 27,
		"OVX" => 45,
		"No dominant order" => 167,
	),
	
	"Order of Adposition and Noun Phrase" => array(
		"Postpositions" => 577,
		"Prepositions" => 512,
		"Inpositions" => 8,
		"No dominant order" => 58,
		"No adpositions" => 30,
	),
	
	"Order of Genitive and Noun" => array(
		"Genitive-Noun" => 685,
		"Noun-Genitive" => 467,
		"No dominant order" => 96,
	),
	
	"Order of Adjective and Noun" => array(
		"Adjective-Noun" => 373,
		"Noun-Adjective" => 878,
		"No dominant order" => 110,
		"Only internally-headed relative clauses" => 5,
	),
	
	"Order of Demonstrative and Noun" => array(
		"Demonstrative-Noun" => 542,
		"Noun-Demonstrative" => 560,
		"Demonstrative prefix" => 9,
		"Demonstrative suffix" => 28,
		"Demonstrative before and after Noun" => 17,
		"Mixed" => 67,
	),
	
	"Order of Numeral and Noun" => array(
		"Numeral-Noun" => 479,
		"Noun-Numeral" => 608,
		"No dominant order" => 65,
		"Numeral only modifies verb" => 2,
	),
	
	"Order of Relative Clause and Noun" => array(
		"Noun-Relative clause" => 580,
		"Relative clause-Noun" => 141,
		"Internally headed" => 24,
		"Correlative" => 7,
		"Adjoined" => 8,
		"Doubly headed" => 1,
		"Mixed" => 64,
	),
	
	"Prenominal relative clauses" => array(
		"Relative clause-Noun (RelN) dominant" => 141,
		"RelN or NRel" => 29,
		"RelN or internally-headed" => 15,
		"RelN or correlative" => 5,
		"RelN or double-headed" => 1,
	),
	
	"Postnominal relative clauses" => array(
		"Noun-Relative clause (NRel) dominant" => 580,
		"NRel or RelN" => 31,
		"NRel or internally-headed" => 8,
		"NRel or correlative" => 2,
	),
	
	"Postnominal relative clauses" => array(
		"Noun-Relative clause (NRel) dominant" => 580,
		"NRel or RelN" => 31,
		"NRel or internally-headed" => 8,
		"NRel or correlative" => 2,
	),
	
	"Internally-headed relative clauses" => array(
		"Internally-headed relative clause dominant" => 24,
		"Internally-headed or RelN" => 15,
		"Internally-headed or NRel" => 8,
		"Internally-headed or correlative" => 1,
		"Internally-headed or double-headed" => 1,
		"Internally-headed occurs as nondominant type" => 10,
		"Internally-headed exists" => 4,
	),
	
	"Correlative relative clauses" => array(
		"Correlative relative clause dominant" => 7,
		"Correlative or RelN" => 7,
		"Correlative or NRel" => 2,
		"Correlative or internally-headed" => 1,
		"Correlative or adjoined" => 2,
		"Correlative as nondominant type" => 3,
		"Correlative exists" => 1,
	),
	
	"Adjoined relative clauses" => array(
		"Adjoined relative clause dominant" => 8,
		"Adjoined or correlative" => 2,
	),
	
	"Order of Degree Word and Adjective" => array(
		"Degree word-Adjective" => 227,
		"Adjective-Degree word" => 192,
		"No dominant order" => 62,
	),
	
	"Position of Polar Question Particles" => array(
		"Initial" => 130,
		"Final" => 313,
		"Second position" => 52,
		"Other position" => 8,
		"In either of two positions" => 25,
		"No question particle" => 355,
	),
	
	"Position of Interrogative Phrases in Content Questions" => array(
		"Initial interrogative phrase" => 264,
		"Not initial interrogative phrase" => 614,
		"Mixed" => 23,
	),
	
	"Order of Adverbial Subordinator and Clause" => array(
		"Initial subordinator word" => 399,
		"Final subordinator word" => 96,
		"Internal subordinator word" => 8,
		"Subordinating suffix" => 64,
		"Mixed" => 93,
	),
	
	"Relationship between the Order of Object and Verb<br /> and the Order of Adposition and Noun Phrase" => array(
		"OV and Postpositions" => 472,
		"OV and Prepositions" => 14,
		"VO and Postpositions" => 42,
		"VO and Prepositions" => 456,
		"Other" => 158,
	),
	
	"Relationship between the Order of Object and Verb<br /> and the Order of Relative Clause and Noun" => array(
		"OV and RelN" => 132,
		"OV and NRel" => 113,
		"VO and RelN" => 5,
		"VO and NRel" => 416,
		"Other" => 213,
	),
	
	"Relationship between the Order of Object and Verb<br /> and the Order of Adjective and Noun" => array(
		"OV and AdjN" => 216,
		"OV and NAdj" => 332,
		"VO and AdjN" => 114,
		"VO and NAdj" => 456,
		"Other" => 198,
	),
	
	"Alignment of Case Marking of Full Noun Phrases" => array(
		"Neutral" => 98,
		"Nominative - accusative (standard)" => 46,
		"Nominative - accusative (marked nominative)" => 6,
		"Ergative - absolutive" => 32,
		"Tripartite" => 4,
		"Active-inactive" => 4,
	),
	
	"Alignment of Case Marking of Pronouns" => array(
		"Neutral" => 79,
		"Nominative - accusative (standard)" => 61,
		"Nominative - accusative (marked nominative)" => 3,
		"Ergative - absolutive" => 20,
		"Tripartite" => 3,
		"Active - inactive" => 3,
		"None" => 3,
	),

	"Alignment of Verbal Person Marking" => array(
		"Neutral" => 84,
		"Accusative" => 212,
		"Ergative" => 19,
		"Active" => 26,
		"Hierarchical" => 11,
		"Split" => 28,
	),
	
	"Expression of Pronominal Subjects" => array(
		"Obligatory pronouns in subject position" => 82,
		"Subject affixes on verb" => 437,
		"Subject clitics on variable host" => 32,
		"Subject pronouns in different position" => 67,
		"Optional pronouns in subject position" => 61,
		"Mixed" => 32,
	),
	
	"Verbal Person Marking" => array(
		"No person marking" => 82,
		"Only the A argument" => 73,
		"Only the P argument" => 24,
		"A or P argument" => 6,
		"Both the A and P arguments" => 193,
	),
	
	"Third Person Zero of Verbal Person Marking" => array(
		"No person marking" => 96,
		"No zero realization" => 181,
		"Zero in some 3sg forms" => 21,
		"Zero in all 3sg forms" => 45,
		"Zero in all 3rd person forms" => 36,
		"Zero only in 3rd nonsingular" => 1,
	),
	
	"Order of Person Markers on the Verb" => array(
		"A and P do not or do not both occur on the verb" => 187,
		"A precedes P" => 96,
		"P precedes A" => 57,
		"Both orders of A and P occur" => 19,
		"A and P are fused" => 20,
	),
	
	"Ditransitive Construction" => array(
		"Indirect-object construction" => 189,
		"Double-object construction" => 83,
		"Secondary-object construction" => 66,
		"Mixed" => 40,
	),
	
	"Reciprocal Constructions" => array(
		"No reciprocals" => 16,
		"Distinct from reflexive" => 99,
		"Mixed" => 16,
		"Identical to reflexive" => 44,
	),
	
	"Passive Constructions" => array(
		"Present" => 162,
		"Absent" => 211,
	),
	
	"Antipassive Constructions" => array(
		"Implicit patient" => 18,
		"Oblique patient" => 30,
		"No antipassive" => 146,
	),
	
	"Productivity of the Antipassive Construction" => array(
		"productive" => 24,
		"partially productive" => 14,
		"not productive" => 2,
		"no antipassive" => 146,
	),
	
	"Applicative Constructions" => array(
		"Benefactive object; both bases" => 16,
		"Benefactive object; only transitive" => 4,
		"Benefactive and other; both bases" => 49,
		"Benefactive and other; only transitive" => 2,
		"Non-benefactive object; both bases" => 9,
		"Non-benefactive object; only transitive" => 1,
		"Non-benefactive object; only intransitive" => 2,
		"No applicative construction" => 100,
	),
	
	"Other Roles of Applied Objects" => array(
		"Instrument" => 17,
		"Locative" => 18,
		"Instrument and locative" => 12,
		"No other roles (= Only benefactive)" => 36,
		"No applicative construction" => 100,
	),
	
	"Periphrastic Causative Constructions" => array(
		"Sequential but no purposive" => 35,
		"Purposive but no sequential" => 68,
		"Both" => 15,
	),
	
	"Nonperiphrastic Causative Constructions" => array(
		"Neither" => 23,
		"Morphological but no compound" => 254,
		"Compound but no morphological" => 9,
		"Both" => 24,
	),
	
	"Negative Morphemes" => array(
		"Negative affix" => 396,
		"Negative particle" => 502,
		"Negative auxiliary verb" => 47,
		"Negative word, unclear if verb or particle" => 73,
		"Variation between negative word and affix" => 21,
		"Double negation" => 120,
	),
	
	"Symmetric and Asymmetric Standard Negation" => array(
		"Symmetric" => 114,
		"Asymmetric" => 53,
		"Both" => 130,
	),
	
	"Subtypes of Asymmetric Standard Negation" => array(
		"A/Fin" => 40,
		"A/NonReal" => 20,
		"A/Cat" => 82,
		"A/Fin and A/NonReal" => 9,
		"A/Fin and A/Cat" => 21,
		"A/NonReal and A/Cat" => 11,
		"Non-assignable" => 114,
	),
	
	"Negative Indefinite Pronouns and Predicate Negation" => array(
		"Predicate negation also present" => 170,
		"No predicate negation" => 11,
		"Mixed behaviour" => 13,
		"Negative existential construction" => 12,
	),
	
	"Polar Questions" => array(
		"Question particle" => 584,
		"Interrogative verb morphology" => 164,
		"Mixture of previous two types" => 15,
		"Interrogative word order" => 13,
		"Absence of declarative morphemes" => 4,
		"Interrogative intonation only" => 173,
		"No interrogative-declarative distinction" => 1,
	),
	
	"Predicative Possession" => array(
		"Locational" => 48,
		"Genitive" => 22,
		"Topic" => 48,
		"Conjunctional" => 59,
		"'Have'" => 63,
	),
	
	"Predicative Adjectives" => array(
		"Verbal encoding" => 151,
		"Nonverbal encoding" => 132,
		"Mixed" => 103,
	),
	
	"Nominal and Locational Predication" => array(
		"Different" => 269,
		"Identical" => 117,
	),
	
	"Zero Copula for Predicate Nominals" => array(
		"Impossible" => 211,
		"Possible" => 175,
	),
	
	"Comparative Constructions" => array(
		"Locational" => 78,
		"Exceed" => 33,
		"Conjoined" => 34,
		"Particle" => 22,
	),
	
	"Relativization on Subjects" => array(
		"Relative pronoun" => 12,
		"Non-reduction" => 24,
		"Pronoun-retention" => 5,
		"Gap" => 125,
	),
	
	"Relativization on Obliques" => array(
		"Relative pronoun" => 13,
		"Non-reduction" => 14,
		"Pronoun-retention" => 20,
		"Gap" => 55,
		"Not possible" => 10,
	),
	
	"'Want' Complement Subjects" => array(
		"Subject is left implicit" => 144,
		"Subject is expressed overtly" => 72,
		"Both construction types exist" => 14,
		"Desiderative verbal affix" => 45,
		"Desiderative particle" => 8,
	),
	
	"Purpose Clauses" => array(
		"Balanced" => 38,
		"Balanced/deranked" => 30,
		"Deranked" => 102,
	),
	
	"'When' Clauses" => array(
		"Balanced" => 84,
		"Balanced/deranked" => 39,
		"Deranked" => 51,
	),
	
	"Reason Clauses" => array(
		"Balanced" => 90,
		"Balanced/deranked" => 37,
		"Deranked" => 42,
	),
	
	"Utterance Complement Clauses" => array(
		"Balanced" => 114,
		"Balanced/deranked" => 18,
		"Deranked" => 11,
	),
	
	"Hand and Arm" => array(
		"Identical" => 228,
		"Different" => 389,
	),
	
	"Finger and Hand" => array(
		"Identical" => 72,
		"Different" => 521,
	),
	
	"Numeral Bases" => array(
		"Decimal" => 125,
		"Hybrid vigesimal-decimal" => 22,
		"Pure vigesimal" => 20,
		"Other base" => 5,
		"Extended body-part system" => 4,
		"Restricted" => 20,
	),
	
	"Number of Non-Derived Basic Colour Categories" => array(
		"3" => 10,
		"3.5" => 3,
		"4" => 9,
		"4.5" => 1,
		"5" => 56,
		"5.5" => 11,
		"6" => 29,
	),
	
	"Number of Basic Colour Categories" => array(
		"3-4" => 20,
		"4.5-5.5" => 26,
		"6-6.5" => 34,
		"7-7.5" => 14,
		"8-8.5" => 6,
		"9-10" => 8,
		"11" => 11,
	),
	
	"Green and Blue" => array(
		"Green vs. blue" => 30,
		"Green/blue" => 68,
		"Black/green/blue" => 15,
		"Black/blue vs. green" => 2,
		"Yellow/green/blue" => 2,
		"Yellow/green vs. blue" => 1,
		"None" => 2,
	),
	
	"Red and Yellow" => array(
		"Red vs. yellow" => 98,
		"Red/yellow" => 15,
		"Yellow/green/blue vs. red" => 3,
		"Yellow/green vs. red" => 1,
		"None" => 3,
	),
	
	"M-T Pronouns" => array(
		"No M-T pronouns" => 200,
		"M-T pronouns, paradigmatic" => 27,
		"M-T pronouns, non-paradigmatic" => 3,
	),
	
	"M in First Person Singular" => array(
		"No m in first person singular" => 177,
		"m in first person singular" => 53,
	),
	
	"N-M Pronouns" => array(
		"No N-M pronouns" => 194,
		"N-M pronouns, paradigmatic" => 25,
		"N-M pronouns, non-paradigmatic" => 11,
	),
	
	"M in Second Person Singular" => array(
		"No m in second person singular" => 152,
		"m in second person singular" => 78,
	),
	
	"Tea" => array(
		"Words derived from Sinitic cha" => 109,
		"Words derived from Min Nan Chinese te" => 81,
		"Others" => 40,
	),
	
	"Para-Linguistic Usages of Clicks" => array(
		"Logical meanings" => 47,
		"Affective meanings" => 71,
		"Other or none" => 25,
	),
	
	"Order of Negative Morpheme and Verb" => array(
		"NegV" => 524,
		"VNeg" => 171,
		"[Neg-V]" => 162,
		"[V-Neg]" => 203,
		"Negative Tone" => 1,
		"Type 1 / Type 2" => 22,
		"Type 1 / Type 3" => 9,
		"Type 1 / Type 4" => 12,
		"Type 2 / Type 3" => 2,
		"Type 2 / Type 4" => 9,
		"Type 3 / Type 4" => 8,
		"Type 3 / Negative Infix" => 1,
		"OptSingleNeg" => 1,
		"ObligDoubleNeg" => 115,
		"OptDoubleNeg" => 80,
		"OptTripleNeg&amp;ObligDoubleNeg" => 5,
		"OptTripleNeg&amp;OptDoubleNeg" => 1,
	),
	
	"Obligatory Double Negation" => array(
		"NegVNeg" => 36,
		"Neg[V-Neg]" => 28,
		"[Neg-V]Neg" => 9,
		"[Neg-V-Neg]" => 27,
		"Negative tone &amp; VNeg" => 1,
		"Negative tone &amp; [Neg-V]" => 2,
		"NegNegV" => 2,
		"Neg[Neg-V]" => 2,
		"VNegNeg" => 2,
		"Type 1 / Type 2" => 1,
		"Type 1 / Type 3" => 1,
		"Type 1 / Type 5" => 1,
		"Type 1 / Type 7" => 1,
		"Type 1 / Type 9" => 1,
		"Type 2 / Type 4" => 1,
		"ObligDoubleNeg&amp;OptTripleNeg" => 5,
	),
	
	"Optional Double Negation" => array(
		"NegV(Neg)" => 11,
		"(Neg)VNeg" => 20,
		"Neg[V(-Neg)]" => 5,
		"(Neg)[V-Neg]" => 5,
		"[Neg-V](Neg)" => 3,
		"[(Neg-)V]Neg" => 2,
		"[Neg-V(-Neg)]" => 5,
		"[(Neg-)V-Neg]" => 6,
		"V(Neg)Neg" => 2,
		"[V-Neg](Neg)" => 2,
		"Neg(Neg)V" => 1,
		"Neg[(Neg-)]V" => 3,
		"NegV&amp;OptChangeVerbStem" => 1,
		"NegV/[Neg-V-Neg]" => 2,
		"VNeg/[Neg-V-Neg]" => 1,
		"[Neg-V]/NegVNeg" => 1,
		"NegV or NegativeTone&amp;VNeg" => 1,
		"NegV/[V-Neg]/Neg[V-Neg]" => 4,
		"NegV/VNeg/NegVNeg" => 2,
		"NegV/[V-Neg]/[Neg-V-Neg]" => 1,
		"[Neg-V]/VNeg/[Neg-V-Neg]" => 1,
		"NegV/[Neg-V]/Neg[Neg-V]" => 1,
		"OptDoubleNeg&amp;OptTripleNeg" => 1,
	),
	
	"Optional Triple Negation" => array(
		"(Neg)[Neg-V-Neg]" => 1,
		"[V-Neg]Neg&amp;OptNegInfix or Pref" => 1,
		"NegVNeg/NegNegVNeg" => 1,
		"Neg[V-Neg]/NegVNeg&amp;NegTone" => 1,
		"Neg[V(-Neg)]Neg/[Neg-V(-Neg)]Neg" => 1,
		"Neg[V-(Neg)](Neg)" => 1,
	),
	
	"Preverbal Negative Morphemes" => array(
		"NegV" => 682,
		"[Neg-V]" => 230,
		"NegV&amp;[Neg-V]" => 23,
		"None" => 391,
	),
	
	"Postverbal Negative Morphemes" => array(
		"VNeg" => 289,
		"[V-Neg]" => 308,
		"VNeg&amp;[V-Neg]" => 18,
		"None" => 711,
	),
	
	"Minor morphological means of signaling negation" => array(
		"NegTone" => 7,
		"NegInfix" => 2,
		"NegStemChange" => 1,
		"None" => 1316,
	),
	
	"Position of Negative Word With Respect to Subject, Object, and Verb" => array(
		"NegSVO" => 10,
		"SNegVO" => 112,
		"SVNegO" => 2,
		"SVONeg" => 81,
		"NegSOV" => 11,
		"SNegOV" => 15,
		"SONegV" => 65,
		"SOVNeg" => 49,
		"NegVSO" => 58,
		"VSNegO" => 1,
		"VSONeg" => 1,
		"NegVOS" => 18,
		"ONegVS" => 3,
		"OVNegS" => 1,
		"OSVNeg" => 1,
		"More than one position" => 91,
		"OptSingleNeg" => 1,
		"ObligDoubleNeg" => 102,
		"OptDoubleNeg" => 67,
		"MorphNeg" => 334,
		"Other" => 168,
	),
	
	"Position of negative words relative to beginning and end of clause<br /> and with respect to adjacency to verb" => array(
		"Beginning, not immed preverbal" => 44,
		"Preverbal, not beginning or immed" => 18,
		"Immed preverbal" => 339,
		"Immed postverbal" => 92,
		"Postverbal, not immed or end" => 1,
		"End, not immed postverbal" => 115,
	),
	
	"Languages with different word order in negative clauses" => array(
		"VSO, but NegSVO" => 6,
		"SVO, but SNegOV" => 3,
		"SVO, but SONegV" => 1,
		"SVO, but SOVNeg" => 1,
		"SVO, but NegVSO" => 1,
		"SVO but SO[V-Neg]" => 1,
		"SVO but SO[Neg-V]" => 1,
		"OSV but NegSVO/O[Neg-V]S" => 1,
		"SVO, but NegSNegOV" => 1,
		"SVO, but SONeg[V-Neg]/SO[Neg-V-Neg]" => 1,
		"SOV but SONeg[V-Neg]/S[Neg-V-Neg] O" => 1,
		"SVO/VSO, but NegSVONeg" => 1,
		"SVO/VSO, but [Neg-V]SO(Neg)" => 1,
		"SVO/SOV, but SVONeg" => 5,
		"SVO/SOV, but SNegVO" => 1,
		"SVO/SOV, but SNegOV" => 1,
		"SVO/SOV, but SOVNeg" => 1,
	),
	
);


echo "<table>\n";
foreach ($data as $ref => $survey) {
	echo "<tr>";
	$chosen = getData($survey);
	echo "<td>$ref : </td> <td>$chosen</td>";
	echo "</tr>\n";
}
echo "</table>\n";
?>

</body>
</html>
