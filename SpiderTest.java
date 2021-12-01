package Spider;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;

import org.openqa.selenium.By;
import org.openqa.selenium.Cookie;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.JavascriptExecutor;

class Nutrition{
	String productName;
	String calories;
	String totalFat;
	String saturatedFat;
	String transFat;
	String cholesterol;
	String sodium;
	String totalCarbohydrate;
	String protein;
}

class Product{
	String productId;//可以用Instacart的关键词
	String productName;
	String productPrice;
	String productType;//就是搜索的那个关键词
	String sellerId;
	String productDescription;//成分表,Serving Size, Servings Per Container
}


public class SpiderTest {
	public static WebDriver webDriver;
	
	public static WebElement getElementByPath(String path){
		WebElement temp = null;
		try{
			temp = webDriver.findElement(By.xpath(path));
		}catch(Exception e) {
			return temp;
		}
		return temp;
	}
	
	public static WebElement getElementByTagName(String tagName){
		WebElement temp = null;
		try{
			temp = webDriver.findElement(By.tagName(tagName));
		}catch(Exception e) {
			return temp;
		}
		return temp;
	}
	
    @SuppressWarnings("unused")
	public static void main(String[] args) throws Exception{
    	
    	Set set = new HashSet();
    	
        System.getProperties().setProperty("webdriver.chrome.driver",
                "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe");
        ChromeOptions options = new ChromeOptions();
        // 无界面参数，使用后不会打开浏览器，linuxx环境必须加入
        options.addArguments("--headless");
        //禁用沙盒
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-gpu");
        options.addArguments("--disable-dev-shm-usage");
        
        Base base = new Base();
        base.configure();
        Cookie c1 = new Cookie("G_ENABLED_IDPS", "google");
        Cookie c2 = new Cookie("__Host-instacart_sid", "JlPLpnAuSYwLKDCxPfamvB09SgmUoBq0qnOsLfjnlNQ");
        Cookie c3 = new Cookie("__stripe_mid","9919485b-7d0e-4ed5-9b03-bed5171b09aac05658");
        Cookie c4 = new Cookie("__stripe_sid", "2bbb0286-1b6f-446f-8eae-841c2608e0768d83ff");
        Cookie c5 = new Cookie("_dd_s","rum=0&expire=1634187256453");
        Cookie c6 = new Cookie("_instacart_logged_in","1");
        Cookie c7 = new Cookie("_instacart_session_id","VXJxR0FtQWc3QlRGUVRzYXBRbjBRRG50bWV4ZHFlQnBkeHFqNlhaQms0dmJVbi9qaENPckpIK2ZzYXl1RHVNS21jOWlMN0IrY2h3QzZydUhXSFZwbDVveW8xRXFyay96cnhhMVQ5U0hRZ1BlckZPYzdoVFNGZ0c3TEZBRWRYN1hQYWVZNmNidjQ5MFRHQldCZkMrQmRIRTYyNFZjdjJydjFsY2VqUWVMYnR5VGdVZk1wdkU4SHpwQU5nMllHY1R4aEV4WVdSVFNra1pxZ2JjSkFIS09KN0FkNXdmN0h0NW5IVExDRGxmbGhaYjJ5RzJEMmRCQ0VGbmpoL0VzQVBSci0tcmRGVWxpUWtwMzNvZ2ZhYkVHMXlOdz09--6fed9b67e275cb1b2a8f0f018163952389e61155");
        Cookie c8 = new Cookie("ahoy_visit","671ed412-1e78-42e9-b4e0-22b8cdd7f469");
        Cookie c9 = new Cookie("ahoy_visitor","68f8ee0e-9f17-4a74-9ac9-5357918c8e67");
        Cookie c10 = new Cookie("build_sha","ada940d3df89d4eeb73f9bc189f5f781ea7802e5");
        Cookie c11 = new Cookie("device_uuid","c6e57f80-78ee-473b-8845-6c626992dcf8");
        Cookie c12 = new Cookie("known_visitor","%7Chgd77813%40outlook.com%7Cemail");
        Cookie c13 = new Cookie("soft_prompt_date_501159344","1634135651827");
        Cookie c14 = new Cookie("__cf_bm","cOIfgKupkMQlFKBHhu5sdMwnm3pivHh9ItIyeKfDEUs-1634185143-0-AVRzWk7kh/cCuZa/7prU/6YlwD/utgdcdlWB9mA5/As/MFWGMcbhh0tKxWkOk0WCWDuzhHM+fos4fgjNngiS6xk=");
        
        Cookie cti1 = new Cookie("lightstep_guid/lite-web","3c5e06fd2201020a");
        Cookie cti2 = new Cookie("lightstep_session_id","707e9e0c1152b77b");
        Cookie cti3 = new Cookie("optimizelyEndUserId","lo_78a4bba1e1f3");
        Cookie cti4 = new Cookie("sid","1:6C64T23lmfJm8xKXwM3NQP8+5j4aFTpiO8pR3ZkinwesifLotQsfcO4+uks91M0vrxQ5a6vkbPATST02H8zhhg==");
        Cookie cti5 = new Cookie("uid","lo_78a4bba1e1f3");
        
        Cookie cic1 = new Cookie("IR_7412","1634184033572%7C0%7C1634184033572%7C%7C");
        Cookie cic2 = new Cookie("IR_gbd","instacart.com");
        Cookie cic3 = new Cookie("__ssid","36084058cf4d601234cbc7e8d558f12");
        Cookie cic4 = new Cookie("_fbp","fb.1.1631314187192.675081317");
        Cookie cic5 = new Cookie("_ga","GA1.2.803745157.1631314186");
        Cookie cic6 = new Cookie("_ga_VL5WVTXMWP","GS1.1.1634186352.20.1.1634186356.0");
        Cookie cic7 = new Cookie("_gac_UA-35642030-3","1.1633738018.CjwKCAjw2P-KBhByEiwADBYWCt77qlGtGiKvJvwr2814aPdhvtHQjbGXuP9DUXVzdAK1p8LGj8D81RoC3UwQAvD_BwE");
        Cookie cic8 = new Cookie("_gcl_au","1.1.427466169.1631314186");
        Cookie cic9 = new Cookie("_gcl_aw","GCL.1633738018.CjwKCAjw2P-KBhByEiwADBYWCt77qlGtGiKvJvwr2814aPdhvtHQjbGXuP9DUXVzdAK1p8LGj8D81RoC3UwQAvD_BwE");
        Cookie cic10 = new Cookie("_gid","GA1.2.1892396595.1634135648");
        Cookie cic11 = new Cookie("_scid","c537d5c0-fb06-4731-afe6-cfe51b6cec45");
        Cookie cic12 = new Cookie("_sctr","1|1633669200000");
        Cookie cic13 = new Cookie("_uetsid","9fd747c02c3211eca4b34ba2898a8db3");
        Cookie cic14 = new Cookie("_uetvid","65791640128911eca5f393186c05b1e8");
        Cookie cic15 = new Cookie("ab.storage.deviceId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d","%7B%22g%22%3A%22a7350d3d-b8a8-3be2-28f0-466e527e7f84%22%2C%22c%22%3A1632038215065%2C%22l%22%3A1632038215065%7D");
        Cookie cic16 = new Cookie("ab.storage.sessionId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d","%7B%22g%22%3A%22237e04d4-97ca-726c-3ad9-ed1c4b370bcc%22%2C%22e%22%3A1634185832491%2C%22c%22%3A1634184032491%2C%22l%22%3A1634184032491%7D");
        Cookie cic17 = new Cookie("ab.storage.userId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d","%7B%22g%22%3A%22501159344%22%2C%22c%22%3A1632038215063%2C%22l%22%3A1632038215063%7D");
        Cookie cic18 = new Cookie("ajs_anonymous_id","6285c401-9b2b-4af1-b3f6-02eb6e3790b0");
        Cookie cic19 = new Cookie("ajs_user_id","501159344");
        Cookie cic20 = new Cookie("forterToken","4b114836f6584333b17a4ef5631c14df_1634184032012__UDF43_9ck");
        Cookie cic21 = new Cookie("ftr_ncd","6");
        Cookie cic22 = new Cookie("impact_radius_click_id","1732890876");
        Cookie cic23 = new Cookie("optimizelyEndUserId","lo_78a4bba1e1f3");
        //Cookie cic24 = new Cookie("","");
        
        
        
        
        
        
        
        
        
        
        webDriver = new ChromeDriver(options);

//        webDriver.manage().window().maximize();
        webDriver.get("https://www.instacart.com/store");
        webDriver.manage().addCookie(c1);
        webDriver.manage().addCookie(c2);
        webDriver.manage().addCookie(c3);
        webDriver.manage().addCookie(c4);
        webDriver.manage().addCookie(c5);
        webDriver.manage().addCookie(c6);
        webDriver.manage().addCookie(c7);
        webDriver.manage().addCookie(c8);
        webDriver.manage().addCookie(c9);
        webDriver.manage().addCookie(c10);
        webDriver.manage().addCookie(c11);
        webDriver.manage().addCookie(c12);
        webDriver.manage().addCookie(c13);
        webDriver.manage().addCookie(c14);
        
        webDriver.manage().addCookie(cti1);
        webDriver.manage().addCookie(cti2);
        webDriver.manage().addCookie(cti3);
        webDriver.manage().addCookie(cti4);
        webDriver.manage().addCookie(cti5);
        
        webDriver.manage().addCookie(cic1);
        webDriver.manage().addCookie(cic2);
        webDriver.manage().addCookie(cic3);
        webDriver.manage().addCookie(cic4);
        webDriver.manage().addCookie(cic5);
        webDriver.manage().addCookie(cic6);
        webDriver.manage().addCookie(cic7);
        webDriver.manage().addCookie(cic8);
        webDriver.manage().addCookie(cic9);
        webDriver.manage().addCookie(cic10);
        webDriver.manage().addCookie(cic11);
        webDriver.manage().addCookie(cic12);
        webDriver.manage().addCookie(cic13);
        webDriver.manage().addCookie(cic14);
        webDriver.manage().addCookie(cic15);
        webDriver.manage().addCookie(cic16);
        webDriver.manage().addCookie(cic17);
        webDriver.manage().addCookie(cic18);
        webDriver.manage().addCookie(cic19);
        webDriver.manage().addCookie(cic20);
        webDriver.manage().addCookie(cic21);
        webDriver.manage().addCookie(cic22);
        webDriver.manage().addCookie(cic23);
        
        /* 
        webDriver.get("https://www.instacart.com/store/items/item_258546856");
        try {
            Thread.sleep(12000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        WebElement tproductName = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[1]/div");
        System.out.println(tproductName.getText().replace("?", ""));
        try {
            Thread.sleep(13000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        */
        webDriver.get("https://www.instacart.com/store");
        
        FileWriter writer1 = new FileWriter(new File("product.txt"));
        BufferedWriter bwProduct = new BufferedWriter(writer1);
        FileWriter writer2 = new FileWriter(new File("nutrition.txt"));
        BufferedWriter bwNutrition = new BufferedWriter(writer2);
        
		FileInputStream inputStream = new FileInputStream("keywords.txt");
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
        String keyword = null;
        Random r = new Random();
        
        List<Nutrition> nutrition = new ArrayList<>();
        List<Product> product = new ArrayList<>();
        Nutrition newNutrition;
        Product newProduct;
        
        int clock = 0;
        
        while((keyword = bufferedReader.readLine()) != null)
		{
        	keyword.replace("聽", "");
        	System.out.println("keyword:"+keyword);
        	
        	String[] keywordSplitString = keyword.split(" ");//分割keyword
        	for(int i = 0; i < keywordSplitString.length; i++) {//去掉以及es
        		if(keywordSplitString[i].length()>=3&&keywordSplitString[i].charAt(keywordSplitString[i].length()-2)=='e'&&keywordSplitString[i].charAt(keywordSplitString[i].length()-1)=='s') {
        			keywordSplitString[i] = keywordSplitString[i].substring(0, keywordSplitString[i].length()-2);
        		}else if(keywordSplitString[i].length()>=2&&keywordSplitString[i].charAt(keywordSplitString[i].length()-1)=='s') {
        			keywordSplitString[i] = keywordSplitString[i].substring(0, keywordSplitString[i].length()-1);
        		}
        	}
        	
        	webDriver.get("https://www.instacart.com/store/costco/storefront");
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            WebElement searchBox = getElementByTagName("input");
            if(searchBox==null) continue;
            searchBox.clear();
            searchBox.sendKeys(keyword);
            searchBox.submit();
            try {
                Thread.sleep(3100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            
            String s1 = "/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/ul[1]/li[";
            String s2 = "]/div/div/div/div/div/a";
            //WebElement theItem = webDriver.findElement(By.xpath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/ul[1]/li[2]/div/div/div/div/div/a"));
            //System.out.println(theItem.getAttribute("class"));
            List<WebElement> itemsTest = webDriver.findElements(By.xpath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/ul[1]/li"));
            if(itemsTest.size()==0) {
            	itemsTest = webDriver.findElements(By.xpath(" /html/body/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[3]/ul[1]/li"));
            	s1 = "/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[3]/ul[1]/li[";
            	s2 = "]/div/div/div/div/div/a";
            }
            if(itemsTest.size()==0) continue;
            List<String> stringItemUrl = new ArrayList<>();           
            System.out.println(itemsTest.size());						
            for(int i = 1; i <= itemsTest.size(); i++) {
            	WebElement theItemHref = getElementByPath(s1+i+s2);
            	if(theItemHref==null) continue;
            	String tempUrl = theItemHref.getAttribute("href");
            	int tempIndex = tempUrl.indexOf("?");
            	stringItemUrl.add(tempUrl.substring(0,tempIndex));
            }
            for(int i = 0; i < stringItemUrl.size(); i++) {
            	System.out.println(stringItemUrl.get(i));
            }
            

            for(int i = 0; i < stringItemUrl.size()&&i<=22; i++) {
            	clock++;
            	if(clock%10==0) bwProduct.flush();
                if(clock%10==0) bwNutrition.flush();
                webDriver.get(stringItemUrl.get(i));
                try {
                    Thread.sleep(1500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                
                newProduct = new Product();
                newNutrition = new Nutrition();
                
                String delimeter = "_";
                String[] temp = stringItemUrl.get(i).split(delimeter);
                System.out.println(temp[temp.length-1]);//productId
                newProduct.productId = temp[temp.length-1];
                if(set.contains(newProduct.productId)) {//有相同Id的直接跳过
                	continue;
                }
                
                									     
                WebElement productName = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[1]/div/div[3]/div[1]/h2/span");            								
                if(productName!=null) {
                	System.out.println(productName.getText());
                	newProduct.productName = productName.getText();
                }else {
                	productName = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[1]/div/div[3]/div[1]/h2/span");            								
                	if(productName!=null) {
                    	System.out.println(productName.getText());
                    	newProduct.productName = productName.getText();
                	}else {
                		continue;
                	}
                }
                
                int keywordFlag = 0;
                for(int kwIndex = 0; kwIndex < keywordSplitString.length&&keywordFlag==0; kwIndex++) {
                	if(newProduct.productName.toLowerCase().contains(keywordSplitString[kwIndex].toLowerCase())) {
                		keywordFlag = 1;
                	}
                }
                
                if(keywordFlag == 0) continue;//假如产品名没有包含keyword,直接跳过
                
                set.add(newProduct.productId);
                
                String newFileName = newProduct.productId + ".png";//图片
                OutputStream os = new FileOutputStream("D:\\Eclipse-workspace\\ZhiLianSpider\\img" + "\\" + newFileName);
                WebElement imgElement = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[1]/div/div[2]/div/div/img");
                if(imgElement==null) {
                	System.out.println("no img");
                }else {
                	String urlStr = imgElement.getAttribute("src");
                	URL url = new URL(urlStr);
                	URLConnection con = url.openConnection();
                	InputStream is = con.getInputStream();
                	int len;
                	byte[] bs = new byte[4096];
                	while ((len = is.read(bs)) != -1) {
                		os.write(bs, 0, len);
                	}
                	os.close();
                	is.close();
                }
                
                
                temp = newProduct.productName.split(" ");
                int i1 = r.nextInt(4);//产生随机数[0,n)
                newProduct.sellerId = "Costco0";// + i1;//随机分配下吧
                
                WebElement productPrice = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[1]/div/div[3]/div[1]/div[2]/div[1]/span");
                if(productPrice!=null) {
                	System.out.println(productPrice.getText());
                	newProduct.productPrice = productPrice.getText();
                }else {
                	System.out.println("unknown");
                	newProduct.productPrice = "unknown";
                }
                
                String t1,t2,t3;                                   
                WebElement productDescription1 = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[1]/div");
                if(productDescription1==null) productDescription1 = getElementByPath(" /html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[6]/div/div/div");
                if(productDescription1!=null) {
                	t1 = productDescription1.getText();
                }else {
                	t1 = "";
                }
                WebElement productDescription2 = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[2]/div/div[1]/div[1]");
                if(productDescription2!=null) {
                	t2 = productDescription2.getText();
                	if(t1=="");
                	else {
                		t2 = "/" + t2;
                	}
                }else {
                	t2 = "";
                }
                WebElement productDescription3 = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[2]/div/div[1]/div[2]");
                if(productDescription3!=null) {
                	t3 = productDescription3.getText();
                	if(t1==""&&t2=="");
                	else t3 = "/" + t3;
                }else {
                	t3 = "";
                }
                
                newProduct.productDescription = t1 + t2 + t3;
                newProduct.productDescription = newProduct.productDescription.replace("\n", ",");
                if((newProduct.productDescription).length()==0) newProduct.productDescription = "unknown";
                System.out.println(newProduct.productDescription);//productDescription
                
                System.out.println(keyword);//productType
                newProduct.productType = keyword;
                product.add(newProduct);
                bwProduct.write(newProduct.productId + "\t" + newProduct.productName + "\t" + newProduct.productPrice + "\t" + newProduct.productType + "\t" + newProduct.sellerId + "\t" + newProduct.productDescription + "\r\n");
                
                System.out.println();
                System.out.println("Nutrition Facts");
                delimeter = " ";
                
                newNutrition.productName = newProduct.productName;
                											
                WebElement exsitnutrition = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[2]/div/div[1]/h3");
                if(exsitnutrition==null)  exsitnutrition = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[6]/div/div/div[2]/div/div[1]/h3");
                if(exsitnutrition==null) continue;    
                WebElement calories = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[2]/div/ul[1]/li[2]");
                if(calories==null) calories = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[6]/div/div/div[2]/div/ul[1]/li[2]");
                if(calories!=null) {
                    temp = calories.getText().split(delimeter);
                    if(temp.length<=0) {
                    	newNutrition.calories = "unknown";
                    	System.out.println("calories:"+newNutrition.calories);
                    }else {
                        System.out.println("calories:"+temp[temp.length - 1]);
                        newNutrition.calories = temp[temp.length - 1];
                    }
                }else {
                	newNutrition.calories = "unknown";
                	System.out.println("calories:"+newNutrition.calories);
                }
                										///html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[6]/div/div/div[2]/div/ul[2]/li[2]/ul/li[1]/span[1]
                WebElement totalFat = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[2]/div/ul[2]/li[2]/ul/li[1]/span[1]");
                if(totalFat==null) totalFat = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[6]/div/div/div[2]/div/ul[2]/li[2]/ul/li[1]/span[1]");
                if(totalFat!=null) {
                	temp = totalFat.getText().split(delimeter);
                	System.out.println(totalFat.getText());
                	if(temp.length<=0) {
                    	newNutrition.totalFat = "unknown";
                    	System.out.println("totalFat:"+newNutrition.totalFat); 
                	}else {
                        temp = temp[temp.length -1].split("\\n");
                    	if(temp.length<=1) {
                    		if(temp[temp.length -1].charAt(temp[temp.length -1].length()-1)!='g') {
                            	newNutrition.totalFat = "unknown";
                            	System.out.println("totalFat:"+newNutrition.totalFat); 
                    		}
                    		else {
                    			newNutrition.totalFat = temp[temp.length - 1];
                    			System.out.println("totalFat:"+temp[temp.length - 1]);
                    		}
                    	}else {
                            System.out.println("totalFat:"+temp[temp.length - 2]); 
                            newNutrition.totalFat = temp[temp.length - 2];
                    	}
                	}
                }else {
                	newNutrition.totalFat = "unknown";
                	System.out.println("totalFat:"+newNutrition.totalFat); 
                }
                
                WebElement saturatedFat = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[2]/div/ul[2]/li[2]/ul/li[2]/span[1]");
                if(saturatedFat==null) saturatedFat = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[6]/div/div/div[2]/div/ul[2]/li[2]/ul/li[2]/span[1]");
                if(saturatedFat!=null) {
                    temp = saturatedFat.getText().split(delimeter);
                    if(temp.length<=0) {
                    	newNutrition.saturatedFat = "unknown";
                    	System.out.println("saturatedFat:"+newNutrition.saturatedFat);
                    }else {
                    	temp = temp[temp.length -1].split("\\n");
                    	if(temp.length<=1) {
                    		if(temp[temp.length -1].charAt(temp[temp.length -1].length()-1)!='g') {
                            	newNutrition.saturatedFat = "unknown";
                            	System.out.println("saturatedFat:"+newNutrition.saturatedFat); 
                    		}
                    		else {
                    			newNutrition.saturatedFat = temp[temp.length - 1];
                    			System.out.println("saturatedFat:"+temp[temp.length - 1]);
                    		}
                    	}else {
                            System.out.println("saturatedFat:"+temp[temp.length - 2]);
                            newNutrition.saturatedFat = temp[temp.length - 2];
                    	}
                    }
                }else {
                	newNutrition.saturatedFat = "unknown";
                	System.out.println("saturatedFat:"+newNutrition.saturatedFat);
                }
                                    
                WebElement transFat = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[2]/div/ul[2]/li[2]/ul/li[3]/span[1]");
                if(transFat==null) transFat = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[6]/div/div/div[2]/div/ul[2]/li[2]/ul/li[3]/span[1]");
                if(transFat != null) {
                    temp = transFat.getText().split(delimeter);
                    if(temp.length<=0) {
                    	newNutrition.transFat = "unknown";
                    	System.out.println("transFat:"+newNutrition.transFat);
                    }else {
                        temp = temp[temp.length -1].split("\\n");
                        System.out.println("transFat:"+temp[temp.length - 1]);
                        newNutrition.transFat = temp[temp.length - 1];
                    }
                }else {
                	newNutrition.transFat = "unknown";
                	System.out.println("transFat:"+newNutrition.transFat);
                }
                WebElement cholesterol = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[2]/div/ul[2]/li[3]/ul/li/span[1]");
                if(cholesterol==null) cholesterol = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[6]/div/div/div[2]/div/ul[2]/li[3]/ul/li/span[1]");
                if(cholesterol != null) {
                    temp = cholesterol.getText().split(delimeter);
                    if(temp.length<=0) {
                    	newNutrition.cholesterol = "unknown";
                    	System.out.println("cholesterol:"+newNutrition.cholesterol);
                    }else {
                    	temp = temp[temp.length -1].split("\\n");
                    	if(temp.length<=1) {
                    		if(temp[temp.length -1].charAt(temp[temp.length -1].length()-1)!='g') {
                            	newNutrition.cholesterol = "unknown";
                            	System.out.println("cholesterol:"+newNutrition.cholesterol); 
                    		}
                    		else {
                    			newNutrition.cholesterol = temp[temp.length - 1];
                    			System.out.println("cholesterol:"+temp[temp.length - 1]);
                    		}
                    	}else {
                            System.out.println("cholesterol:"+temp[temp.length - 2]);
                            newNutrition.cholesterol = temp[temp.length - 2];
                    	}
                    }
                }else {
                	newNutrition.cholesterol = "unknown";
                	System.out.println("cholesterol:"+newNutrition.cholesterol);
                }
                WebElement sodium = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[2]/div/ul[2]/li[4]/ul/li/span[1]");
                if(sodium==null) sodium = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[6]/div/div/div[2]/div/ul[2]/li[4]/ul/li/span[1]");
                if(sodium != null) {
                    temp = sodium.getText().split(delimeter);
                    if(temp.length<=0) {
                    	newNutrition.sodium = "unknown";
                    	System.out.println("sodium:"+newNutrition.sodium);
                    }else {
                    	temp = temp[temp.length -1].split("\\n");
                    	if(temp.length<=1) {
                    		if(temp[temp.length -1].charAt(temp[temp.length -1].length()-1)!='g') {
                    			newNutrition.sodium = "unknown";
                            	System.out.println("sodium:"+newNutrition.sodium);
                    		}
                    		else {
                    			newNutrition.sodium = temp[temp.length - 1];
                    			System.out.println("sodium:"+temp[temp.length - 1]);
                    		}
                    	}else {
                            System.out.println("sodium:"+temp[temp.length - 2]);
                            newNutrition.sodium = temp[temp.length - 2];
                    	}
                    }
                }else {
                	newNutrition.sodium = "unknown";
                	System.out.println("sodium:"+newNutrition.sodium);
                }
               
                WebElement totalCarbohydrate = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[2]/div/ul[2]/li[5]/ul/li/span[1]");
                if(totalCarbohydrate==null)  totalCarbohydrate = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[6]/div/div/div[2]/div/ul[2]/li[5]/ul/li[1]/span[1]");
                if(totalCarbohydrate!=null) {
                    temp = totalCarbohydrate.getText().split(delimeter);
                    if(temp.length <= 0) {
                    	newNutrition.totalCarbohydrate = "unknown";
                    	System.out.println("totalCarbohydrate:"+newNutrition.totalCarbohydrate);
                    }else {
                    	temp = temp[temp.length -1].split("\\n");
                    	if(temp.length<=1) {
                    		if(temp[temp.length -1].charAt(temp[temp.length -1].length()-1)!='g') {
                            	newNutrition.totalCarbohydrate = "unknown";
                            	System.out.println("totalCarbohydrate:"+newNutrition.totalCarbohydrate);
                    		}
                    		else {
                    			newNutrition.totalCarbohydrate = temp[temp.length - 1];
                    			System.out.println("totalCarbohydrate:"+temp[temp.length - 1]);
                    		}
                    	}else {
                            System.out.println("totalCarbohydrate:"+temp[temp.length - 2]);
                            newNutrition.totalCarbohydrate = temp[temp.length - 2];
                    	}
                    }
                }else {
                	newNutrition.totalCarbohydrate = "unknown";
                	System.out.println("totalCarbohydrate:"+newNutrition.totalCarbohydrate);
                }
                
                
                WebElement protein = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[7]/div/div/div[2]/div/ul[2]/li[6]/ul/li/span[1]");
                if(protein==null) protein = getElementByPath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[6]/div/div/div[2]/div/ul[2]/li[6]/ul/li/span[1]");
                if(protein!=null) {
                    temp = protein.getText().split(delimeter);
                    if(temp.length <= 0) {
                    	newNutrition.protein = "unknown";
                    	System.out.println("protein:" + newNutrition.protein);
                    }else {
                        System.out.println("protein:"+temp[temp.length - 1]);
                        newNutrition.protein = temp[temp.length - 1];
                    }
                }else {
                	newNutrition.protein = "unknown";
                	System.out.println("protein:" + newNutrition.protein);
                }
                nutrition.add(newNutrition);
                System.out.println();
                bwNutrition.write(newNutrition.productName + "\t" + newNutrition.calories + "\t" + newNutrition.totalFat + "\t" + newNutrition.saturatedFat + "\t" + newNutrition.transFat + "\t" + newNutrition.cholesterol + "\t" + newNutrition.sodium + "\t" + newNutrition.totalCarbohydrate + "\t" + newNutrition.protein + "\r\n");

            }
		}
        

		inputStream.close();
		bufferedReader.close();
		bwProduct.close();
        writer1.close();
        bwNutrition.close();
        writer2.close();
        
        File f=new File("D:\\Eclipse-workspace\\ZhiLianSpider\\a.txt");
        FileOutputStream fos1=new FileOutputStream(f);
        OutputStreamWriter dos1=new OutputStreamWriter(fos1);
        dos1.write(webDriver.getPageSource());
        dos1.close();
        System.out.println("get");
        //System.out.println(webDriver.getPageSource());
        //webDriver.
        //System.out.println(stext);
        webDriver.close();

    }

}
