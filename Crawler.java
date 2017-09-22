import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.commons.lang3.StringEscapeUtils;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;


public class Crawler {

	public static void main(String args[]) throws IOException {
		
		List<String[]> list1 = getSymbolDetails("https://www.sports-reference.com/olympics/athletes/");
		System.out.println(list1);
		File file = new File("output.txt");
		StringBuilder builder = new StringBuilder("");
		FileWriter fw=new FileWriter("G:\\testout.csv");
		for(String[] arr: list1) {
			    
	         String fileName;  
			if(!arr[0].equals("DONTPRINT")) {
				System.out.print(StringEscapeUtils.escapeCsv(arr[0]) +",");
				fileName = StringEscapeUtils.escapeCsv(arr[0]) +",";
			}else{
				fileName = " " +",";
				System.out.print(" " +",");
			}
			builder.append(fileName);
			builder.append(StringEscapeUtils.escapeCsv(arr[1]) +",");
			builder.append(StringEscapeUtils.escapeCsv(arr[2]) +",");
			builder.append(StringEscapeUtils.escapeCsv(arr[3]) +",");
			builder.append(StringEscapeUtils.escapeCsv(arr[4]) +",");
			builder.append(StringEscapeUtils.escapeCsv(arr[5]) +",");
			builder.append(StringEscapeUtils.escapeCsv(arr[6]) +",");
			builder.append(StringEscapeUtils.escapeCsv(arr[7]) +",");
			builder.append(StringEscapeUtils.escapeCsv(arr[8]) +",");
			builder.append(StringEscapeUtils.escapeCsv(arr[9]) +",");
			builder.append(StringEscapeUtils.escapeCsv(arr[10]) + "\n" );
			System.out.println(StringEscapeUtils.escapeCsv(arr[1]) +","+
					StringEscapeUtils.escapeCsv(arr[2]) +","+
					StringEscapeUtils.escapeCsv(arr[3]) +","+
					StringEscapeUtils.escapeCsv(arr[4]) +","+
					StringEscapeUtils.escapeCsv(arr[5]) +","+
					StringEscapeUtils.escapeCsv(arr[6]) +","+
					StringEscapeUtils.escapeCsv(arr[7]) +","+
					StringEscapeUtils.escapeCsv(arr[8]) + ","+
					StringEscapeUtils.escapeCsv(arr[9]) +","+
					StringEscapeUtils.escapeCsv(arr[10]) );
			    
	           
		}
		fw.write(builder.toString());
		fw.close(); 
	}
	private static List<String[]> getSymbolDetails(String innerLink) throws IOException {
		Document doc1 = Jsoup.connect(innerLink).get();
		Element element = doc1.getElementById("initial_list");
		String[] arr = new String[4];
		Elements elements2 = element.getElementsByTag("a");
		List<String[]> result = new ArrayList<String[]>();
		int counter = 0;
		for(int i=0;i<elements2.size();i++) {
			if(i<=216 )
				continue;
			if(i>240)
				break;
			if(elements2.get(i).attr("href").startsWith("/olympics/athletes/")) {
				try{
					result.addAll(getPlayerList(elements2.get(i).attr("href")));
				}catch(Exception e) {
					e.printStackTrace();
				}
			}
		}
		return result;	
	}
	
	private static List<String[]> getPlayerList(String innerLink) throws IOException {
		String baseUrl = "https://www.sports-reference.com";
		List<String[]> result = new ArrayList<String[]>();

		Document doc1 = Jsoup.connect(baseUrl+innerLink).get();
		Elements elements = doc1.getElementsByClass("margin_top small_text");
		
		
		
		if(elements != null && elements.size() > 0) {
			String players = elements.get(0).html();
			String regexString = Pattern.quote("</a>") + "(.*?)" + Pattern.quote("<br>");
			Pattern pattern = Pattern.compile(regexString);
			Matcher matcher = pattern.matcher(players);
			List<String> playerDobs = new ArrayList<String>();
			while (matcher.find()) {
			  String textInBetween = matcher.group(1); // Since (.*?) is capturing group 1
			  // You can insert match into a List/Collection here
			  playerDobs.add(textInBetween);
			}
			Elements elements2 = elements.get(0).getElementsByTag("a");
			String playerName = "";
			for(int i=0;i<elements2.size();i++) {
				//playerName = elements2.get(i).text();
				playerName = elements2.get(i).text() + " "+playerDobs.get(i).trim();
				System.out.println(playerName);
				String newLink = elements2.get(i).attr("href");
				result.addAll(getProfileDetails(playerName, newLink));
			}
		}
		
		return result;
		
	}
	
	private static List<String[]> getProfileDetails(String playerName, String innerLink) throws IOException {
		String baseUrl = "https://www.sports-reference.com";
		
		List<String[]> result = new ArrayList<String[]>();
		Document doc1 = Jsoup.connect(baseUrl+innerLink).get();
		Element element = doc1.getElementById("results");
		
		if(element != null ) {
			Elements elements2 = element.getElementsByTag("tr");
			for(int i=0;i<elements2.size();i++) {
				if(i == 0)
					continue;
				String[] arr = new String[11];
				if(i == 1) {
					arr[0] = playerName;
				}else{
					arr[0] = "DONTPRINT";
				}
				
				Elements elements3 = elements2.get(i).getElementsByTag("td");
				for(int j=0;j<elements3.size();j++) {
					
					arr[j+1] = elements3.get(j).text();
				}
				result.add(arr);
			}
			
		}
		return result;
		
	}
}
