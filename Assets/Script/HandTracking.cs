using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 
public class HandTracking : MonoBehaviour
{
    // Start is called before the first frame update
    public UDPReceive udpReceive;
    public GameObject[] handPoints;
    void Start()
    {
        
    }
 
    // Update is called once per frame
    void Update()
    {
        string data = udpReceive.data;
 
        data = data.Remove(0, 1);
        data = data.Remove(data.Length-1, 1);
        //print(data);
        string str=data.Substring(data.IndexOf(",")+1);
        str=str.Substring(str.IndexOf(",")+1);
        str=str.Substring(str.IndexOf(",")+1);

        string[] points = str.Split(',');
 
        //0        1*3      2*3
        //x1,y1,z1,x2,y2,z2,x3,y3,z3
        print(points.Length);
        for ( int i = 0; i<points.Length/3; i++)
        {
                float x = 7-float.Parse(points[i * 3])/100;
                float y = float.Parse(points[i * 3 + 1]) / 100;
                float z = float.Parse(points[i * 3 + 2]) / 100;

                
                handPoints[i].gameObject.SetActive(true);
                handPoints[i].gameObject.GetComponent<PointsLife>().ResetTimer();
                handPoints[i].transform.localPosition = Vector3.Lerp( handPoints[i].transform.localPosition, new Vector3(x, y, z), 10 * Time.deltaTime);
            
 
        }

 
 
    }
}