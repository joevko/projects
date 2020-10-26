import java.nio.file.*;
import java.io.*;
import java.util.*;


import java.util.*;
import java.io.*;


public class Legesystem{
    // Opprett lister som lagrer objektene i legesystemet

	Lenkeliste<Legemiddel> legemidler;
	SortertLenkeliste<Lege> leger;
	Lenkeliste<Pasient> pasienter;
	Lenkeliste<Resept> resepter;

    public static void main(String[] args){
        Legesystem system = new Legesystem();
        if (args.length > 0) {
        	File fil = new File(args[0]);
        	system.lesFraFil(fil);
        	system.hovedmeny();
        } else {
        	System.out.println("Starter med tomt legesystem");
        }
    }

    public void hovedmeny(){
    System.out.println("Hovedmeny");
    System.out.println("1. Oversikt over pasienter, leger, legemidler og resepter");
    System.out.println("2. Legg til legemiddel");
    System.out.println("3. Legg til lege");
    System.out.println("4. Legg til pasient");
    System.out.println("5. Legg til resept");
    System.out.println("6. Bruk en resept til en pasient");
    System.out.println("7. Statistikk");
    System.out.println("8. Avslutt");

    Scanner scan = new Scanner(System.in);
    String valg = scan.nextLine();

		int v = Integer.parseInt(valg);
    if(v < 1 || v > 8){
      System.out.println("Feil meny valg, tast inn mellom 1 og 8");
			hovedmeny();
		}

      switch(v){
        case 1: oversikt();
                hovedmeny();
                break;
        case 2: leggTilLegemiddel();
                hovedmeny();
                break;
        case 3: leggTilLege();
                hovedmeny();
                break;
        case 4: leggTilPasient();
                hovedmeny();
                break;
        case 5: leggTilResept();
                hovedmeny();
                break;
        case 6: brukResept();
                hovedmeny();
                break;
				case 7: reseptStatistikks();
				        hovedmeny();
				        break;

        case 8: return;
      }
    }

    public Legesystem () {
    	this.legemidler = new Lenkeliste<Legemiddel>();
    	this.pasienter = new Lenkeliste<Pasient>();
    	this.resepter = new Lenkeliste<Resept>();
    	this.leger = new SortertLenkeliste<Lege>();
    }


   public  void leggTilLege(){
        System.out.println("Oppgi \"navn, kontrollID\" feks \"Dr Cox, 0\"");
        Scanner scan = new Scanner(System.in);
        String legen = scan.nextLine();
        parseLegerLine(legen);
    }

    public  void leggTilPasient(){
        System.out.println("Oppgi \"navn, fnr\" feks \"Jens Hans Olsen, 11111143521 \"");
        Scanner scan = new Scanner(System.in);
        String pasienten = scan.nextLine();
        parsePasienterLine(pasienten);
    }

    public  void leggTilResept(){
        System.out.println("Oppgi \"legemiddelNummer, legeNavn, pasientId, reit \" feks \"1, Dr. Cox, 2, 3 \"");
        Scanner scan = new Scanner(System.in);
        String resepten = scan.nextLine();
        parseResepterLine(resepten);
    }

    public  void leggTilLegemiddel(){
        System.out.println("Oppgi \"navn, type, pris, virkestoff [, styrke] \" feks \"Predizol, a, 450, 75, 8 \"");
        Scanner scan = new Scanner(System.in);
        String legemiddelen = scan.nextLine();
        parseLegemidlerLine(legemiddelen);
    }

    public  void brukResept(){
        System.out.println("Hvilken pasient vil du se resepter for?");
        for(Pasient p:pasienter){
            System.out.println(p.hentId()+": " + p );
        }
        Scanner scan = new Scanner(System.in);
        String valg = scan.nextLine();
      	int v = Integer.parseInt(valg);

				if(v > pasienter.stoerrelse()-1){
					System.out.println("Feil valg av pasient");
					hovedmeny();
				}
        Pasient reseptPasient = null;
        for(Pasient p : pasienter){
          if(p.hentId() == v){
            reseptPasient = p;
          }
				}
				System.out.println("Du har valgt pasient " + reseptPasient.hentNavn());
				//Stabel<Resept> reseptAaBruke = reseptPasient.hentResepter();
					System.out.println("Hvilken resept vil du bruke");
			  for(Resept r : reseptPasient.hentResepter()){
		        System.out.println(r.hentId()+": " + r.hentLegemiddel().hentNavn()+"(" + r.hentReit() + " reit" + ")" );
		    }

		    String valg2 = scan.nextLine();
				int v2 = Integer.parseInt(valg2);

				if(v2 > reseptPasient.hentResepter().stoerrelse()-1){
 				 System.out.println("Feil valg av resept");
		      hovedmeny();
		      return;
		    }
		    //int v2 = Integer.parseInt(valg2);
		    for(Resept r : resepter){
		      if(r.hentId() == v2){
		        r.bruk();
		      }
		    }
    }

    public  void oversikt () {
    	for (Legemiddel l : this.legemidler) {
    		System.out.println("#"+ l.hentId() + " navn " + l.hentNavn());
    	}
    	this.skrivLegeRapport();
    	this.skrivPasientRapport();
    	this.skrivReseptRapport();
    }

	
    private void reseptStatistikks() {
      int vane = 0;
      int nark = 0;

      for(Resept r : this.resepter) {
          
          if (r.hentLegemiddel() instanceof PreparatA) {
            vane++;
          }else if(r.hentLegemiddel() instanceof PreparatB){
            nark++;
          
        }
      }
      
      System.out.println("narkotiske: " + nark + " vanedannende: " + vane);
      
      for(Lege l : this.leger) {
        int antallNarkotisk = 0;
        if ((antallNarkotisk = l.antallUtskrevneNarkotiskeLegemidler()) > 0) {
          System.out.println(l.hentLegeNavn() + " - Antall utskrevende narkotiske legemidler: " + antallNarkotisk);
        }
      }
    }


    private void skrivPasientRapport () {
    	System.out.println("\nPasienter i systemet:");
    	for (Pasient p : this.pasienter) {
    		System.out.println("#" + p.hentId() + " " + p.hentNavn() + " (" + p.foedselsnr() + ") ");
    	}
    	System.out.println();
    }

     private void skrivLegeRapport() {
    	System.out.println("\nLeger i systemet:");
    	for (Lege l : this.leger) {
    		System.out.println("#" +  " " + l.hentLegeNavn());
    	}
    	System.out.println();
    }

    private void skrivReseptRapport() {
    	System.out.println("\nResepter i systemet:");
    	for (Resept r : this.resepter) {
    		System.out.println("#" + r.hentId() + " " + r.hentLege() + " " + r.hentPasientId() + " " + r.hentReit());
    	}
    	System.out.println();
    }

    private Pasient hentPasient(int id) {
    	for (Pasient p : this.pasienter) {
    		if (p.hentId() == id) {
    			return p;
    		}
    	}
    	return null;
    }

    private Lege hentLege(String navn) {
    	for (Lege l : this.leger) {
    		if (l.hentLegeNavn().equals(navn)) {
    			return l;
    		}
    	}
    	return null;
    }

    private Legemiddel hentLegemiddel(int id) {
    	for (Legemiddel l : this.legemidler) {
    		if (l.hentId() == id) {
    			return l;
    		}
    	}
    	return null;
    }

	 // Parser linje for pasienter og oppretter pasientobjekter
	public  void parsePasienterLine(String line) {
		String[] pasient = line.split(",");
		String navn = pasient[0].trim();
		String fnr = pasient[1].trim();
		Pasient p = new Pasient(navn, fnr);
		//Lenkeliste
		this.pasienter.leggTil(p);
	}

	// Parse linje for legemidler og oppretter legemiddelobjekter
	public  void parseLegemidlerLine(String line) {
		String[] legemiddel = line.split(",");
		String navn = legemiddel[0].trim();
		String type = legemiddel[1].trim();
		double pris = Double.parseDouble(legemiddel[2].trim());
		double virkestoff = Double.parseDouble(legemiddel[3].trim());
		int styrke = 0;
		if (legemiddel.length == 5) {
			styrke = Integer.parseInt(legemiddel[4].trim());
		}
		Legemiddel l = null;
		switch (type) {
			case "a":
				l = new PreparatA(navn, pris, virkestoff, styrke);
				break;
			case "b":
				l = new PreparatB(navn, pris, virkestoff, styrke);
				break;
			case "c":
				l = new PreparatC(navn, pris, virkestoff);
				break;
			default:
				break;
		}
		//Lenkeliste
		this.legemidler.leggTil(l);
	}

	 //Parser linje for leger og oppretter legeobjekter
	public  void parseLegerLine(String line) {
		String[] lege = line.split(",");
		String navn = lege[0].trim();
		int kontrollId = Integer.parseInt(lege[1].trim());

		Lege l = null;
		if (kontrollId == 0) {
			l = new Lege(navn);
		} else {
			l = new Spesialist(navn, kontrollId);
		}
		//SortertLenkeliste
		this.leger.leggTil(l);
	}


	 // Parser linje for resepter og oppretter reseptobjekter
	public  void parseResepterLine(String line) {
		String[] resept = line.split(",");
		int legemiddelNummer = Integer.parseInt(resept[0].trim());
		String legeNavn = resept[1].trim();
		int pasientId = Integer.parseInt(resept[2].trim());
		int reit = Integer.parseInt(resept[3].trim());
		Lege l = this.hentLege(legeNavn);
		Pasient p = this.hentPasient(pasientId);
		Legemiddel legemiddel = this.hentLegemiddel(legemiddelNummer);
		try {
			Resept r = l.skrivResept(legemiddel, p, reit);
			this.resepter.leggTil(r);
		} catch (UlovligUtskrift e) {
		}

	}

	private  void lesFraFil(File fil){
		Scanner scanner = null;
    try{
      	scanner = new Scanner(fil);
    }catch(FileNotFoundException e){
        System.out.println("Fant ikke filen, starter opp som et tomt Legesystem");
        return;
    }

    String innlest = scanner.nextLine();

    while(scanner.hasNextLine()){

      String[] info = innlest.split(" ");

      // Legger til alle pasientene i filen
      if(info[1].compareTo("Pasienter") == 0){
        while(scanner.hasNextLine()) {
          innlest = scanner.nextLine();

  				//Om vi er ferdig med å legge til pasienter, bryt whileløkken,
          //slik at vi fortsetter til koden for å legge til legemiddler
          if(innlest.charAt(0) == '#'){
            break;
          }
          this.parsePasienterLine(innlest); //vanlig lenkeliste
        }
      }
      //Legger inn Legemidlene
      else if(info[1].compareTo("Legemidler") == 0){
        while(scanner.hasNextLine()){
          innlest = scanner.nextLine();
          //Om vi er ferdig med å legge til legemidler, bryt whileløkken,
          //slik at vi fortsetter til koden for å legge til leger
          if(innlest.charAt(0) == '#'){
            break;
          }
          this.parseLegemidlerLine(innlest); //lenkeliste
        }
      }
      //Legger inn leger
      else if(info[1].compareTo("Leger") == 0){
        while(scanner.hasNextLine()){
          innlest = scanner.nextLine();
            //Om vi er ferdig med å legge til leger, bryt whileløkken,
            //slik at vi fortsetter til koden for å legge til resepter
          if(innlest.charAt(0) == '#'){
              break;
          }
          this.parseLegerLine(innlest); //sortert lenkeliste
        }
      }
      //Legger inn Resepter
      else if(info[1].compareTo("Resepter") == 0){
        while(scanner.hasNextLine()){
            innlest = scanner.nextLine();
            this.parseResepterLine(innlest);
        }
      }
  	}
	}
}
