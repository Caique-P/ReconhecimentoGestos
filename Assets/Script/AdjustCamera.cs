using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AdjustCamera : MonoBehaviour
{
    public GameObject[] DistancePoints;
    public GameObject[] Lines;
    public Camera Camera;
    public Vector3 InitialScale;
        // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //Distance / lenght
        //DistancePoints[0] == RightUp
        //DistancePoinst[1] == LeftDown
        Vector3 positionupleft = new Vector3( DistancePoints[1].transform.position.x, DistancePoints[0].transform.position.y, DistancePoints[1].transform.position.z);
        Vector3 positionupright = new Vector3( DistancePoints[0].transform.position.x, DistancePoints[0].transform.position.y, DistancePoints[1].transform.position.z);
        Vector3 positiondownleft = new Vector3( DistancePoints[1].transform.position.x, DistancePoints[1].transform.position.y, DistancePoints[1].transform.position.z);
        Vector3 positiondownright = new Vector3( DistancePoints[0].transform.position.x, DistancePoints[1].transform.position.y, DistancePoints[1].transform.position.z);
   
        float DistanceUp = Vector3.Distance(positionupleft, positionupright);
        float DistanceRight = Vector3.Distance(positionupright, positiondownright);
        float DistanceLeft = Vector3.Distance(positionupleft, positiondownleft);
        float DistanceDown = Vector3.Distance(positiondownleft, positiondownright);

        Vector3 middlePointUp = (positionupleft + positionupright) / 2f;
        Vector3 middlePointRight  = (positionupright + positiondownright) / 2f;
        Vector3 middlePointLeft = (positionupleft + positiondownleft) / 2f;
        Vector3 middlePointDown = (positiondownleft + positiondownright) / 2f;
        
      
        
         float x = Vector3.Distance(Vector3.zero, Camera.main.transform.position);
         float y = DistanceLeft / 2f;
         float requiredFOV = Mathf.Atan(y / x) * Mathf.Rad2Deg;
        
         if(Camera.main.fieldOfView < requiredFOV * 2f){
            Camera.transform.position = new Vector3(middlePointDown.x, middlePointLeft.y, Camera.gameObject.transform.position.z );
            Lines[0].transform.localScale = new Vector3(InitialScale.x, DistanceUp/2, InitialScale.z );
            Lines[1].transform.localScale = new Vector3(InitialScale.x, DistanceRight/2, InitialScale.z );
            Lines[2].transform.localScale = new Vector3(InitialScale.x, DistanceLeft/2, InitialScale.z );
            Lines[3].transform.localScale = new Vector3(InitialScale.x, DistanceDown/2, InitialScale.z );

            Lines[0].transform.position = middlePointUp;
            Lines[1].transform.position = middlePointRight;
            Lines[2].transform.position = middlePointLeft;
            Lines[3].transform.position = middlePointDown;
            Camera.main.fieldOfView = requiredFOV * 2f;
         }
    }
}
