using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace ComputerSearch
{
    public static class ListIds
    {
        [FunctionName("ListIds")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", Route = null)] HttpRequest req,
            ILogger log)
        {
            log.LogInformation("ListIds called");

            string name = req.Query["name"];
            switch (name){
                case "red":
                    return new OkObjectResult(new int[] { 12, 34 });
                case "green":
                    return new OkObjectResult(new int[] { 42 });
            }
            return new OkObjectResult(new int[]{});
        }
    }
    
    public static class GetComputer
    {
        [FunctionName("GetComputer")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", Route = null)] HttpRequest req,
            ILogger log)
        {
            log.LogInformation("ListIds called");

            string id = req.Query["id"];
            switch (id){
                case "12":
                    return new OkObjectResult(new { 
                        name = "red", 
                        cpu = 2, 
                        vendor = "hp" 
                    });
                case "34":
                    return new OkObjectResult(new { 
                        name = "red", 
                        cpu = 2, 
                        vendor = "dell" 
                    });
                case "42":
                    return new OkObjectResult(new { 
                        name = "green", 
                        cpu = 2, 
                        vendor = "apple" 
                    }); 
            }
            return new OkObjectResult(new {});
        }
    }
}
