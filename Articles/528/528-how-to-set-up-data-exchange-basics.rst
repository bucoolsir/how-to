
.. meta::
   :description: How to set up data exchange within your AIMMS application.
   :keywords: aimms, data, exchange

How to integrate the Data Exchange Library
============================================

The Data Exchange Library (DEX) allows you to connect data in a given format (like JSON, XML, table-based CSV/Excel) to your AIMMS model by using a mapping file. These data formats are often used in REST APIs to communicate data. You can find more documentation on the Data Exchange Library via `this link <https://documentation.aimms.com/dataexchange/index.html>`_.

For this how-to we will be working with the example that can be found as a download in `this tutorial <https://academy.aimms.com/mod/page/view.php?id=521>`_, where we build an optimization model to find the least-cost solution. Instead of integrating the data from an Excel file or from a database, we will be integrating the needed data from a JSON-file and use a mapping file to get the data to the correct identifier(s). The basic setup in this how-to can however be implemented for any tree-based data format.


Prerequisites
--------------

#. Make sure you have the Data Exchange Library installed. Visit `this article <https://documentation.aimms.com/general-library/getting-started.html>`__ for instructions on how to do this.

#. Have a mapping file ready and place it somewhere in your project, preferably in a folder called 'Mappings'. Visit `this article <https://documentation.aimms.com/dataexchange/mapping.html>`__ to read more about mappings and how to write one for your specific situation. Note that you can also `generate a mapping file automatically for your project <https://documentation.aimms.com/dataexchange/standard.html#creating-your-own-annotation-based-formats>`__. We will be doing this in the next step.

#. Have a data file ready and place it somewhere in your project, preferably in a folder called 'data'. This is the data you want to read into the model. In our example we've created a JSON data file based on the same data in the tutorial and for testing purposes we've shortened the list so there are only two cities in it. The contents of our file look like this:

.. code-block:: json

    [
		{
			"city": "Qal eh-ye Now",
			"city_ascii": "Qal eh-ye",
			"country": "Afghanistan",
			"iso2": "AF",
			"iso3": "AFG",
			"lat": 34.98300013,
			"lng": 63.13329964,
			"pop": 2997.0,
			"province": "Badghis"
		},
		{
			"city": "Chaghcharan",
			"city_ascii": "Chaghcharan",
			"country": "Afghanistan",
			"iso2": "AF",
			"iso3": "AFG",
			"lat": 34.5167011,
			"lng": 65.25000063,
			"pop": 15000.0,
			"province": "Ghor"
		}
	]


Generate mapping file
-----------------------
The easiest way to get a template for your mapping based on your current model, is to auto-generate a mapping through the :any:`dex::GenerateDatasetMappings` function. This generates standardized table- and Excelsheet mappings based on the ``dex::Dataset``, ``dex::TableName``, and ``dex::ColumnName`` annotations. The generated mappings are then stored in the ``Mappings/Generated`` subfolder of the project folder.

In this example we needed to add the Dataset/TableName/ColumnName annotations to the related identifiers. We were only able to do so by moving the identifiers (holding the same index) that are relevant for our JSON data file into a new declaration and assign the correct dex annotations to this declaration. For the parameter identifiers we've added column-names. 

.. image:: images/data-exchange-1.png
   :scale: 70
   :align: center

*The annotations on declaration-level*

.. image:: images/data-exchange-2.png
   :scale: 70
   :align: center

*The annotations on identifier-level*

After auto-generating the mappings by running the :any:`dex::GenerateDatasetMappings` procedure, we can find the mapping file for JSON sparse mapping. Without edits, it looks like this:

.. code-block:: xml

	<AimmsJSONMapping>
		<ObjectMapping>
			<ArrayMapping name="rows">
				<ObjectMapping>
					<ValueMapping name="l" binds-to="l" />
					<ValueMapping name="lat" maps-to="P_Latitude(l)" />
					<ValueMapping name="lng" maps-to="P_Longitude(l)" />
					<ValueMapping name="pop" maps-to="P_Population(l)" />
				</ObjectMapping>
			</ArrayMapping>
		</ObjectMapping>
	</AimmsJSONMapping>


We have to make a few small changes to this file, as we are working with an array-oriented dataset that holds objects. Hence we removed the first ``<ObjectMapping>`` tag. We can also remove the "name=rows" element from the ``<ArrayMapping>`` tag. Furthermode we had to change the name 'l' to 'city' for the first ``<ValueMapping>>`` as that is the correct name of the property in the JSON file. We couldn't define this name in the annotations within the model as this specific identifier is a set that refers to an index:

.. code-block:: xml

	<AimmsJSONMapping>
		<ArrayMapping>
			<ObjectMapping>
				<ValueMapping name="city" binds-to="l" />
				<ValueMapping name="lat" maps-to="P_Latitude(l)" />
				<ValueMapping name="lng" maps-to="P_Longitude(l)" />
				<ValueMapping name="pop" maps-to="P_Population(l)" />
			</ObjectMapping>
		</ArrayMapping>
	</AimmsJSONMapping>


We saved the file under the same name and are now ready to use it in our basic setup.


Basic setup
--------------

.. note::

        All functions from the library are referenced and described on `this page <https://documentation.aimms.com/dataexchange/api.html>`__.

For this how-to we use the above-mentioned JSON-based data file that holds data from two cities. For every city in the array we will need the name, latitude, longitude and the population and match these items to their respective identifiers in the model, as defined in the mapping file.

To use the mapping in a procedure, you must first read the mapping file into your model. You do this by setting up a procedure in which you call the :any:`dex::AddMapping` function.

After this is done without errors or warnings, you can use the :any:`dex::ReadFromFile` function to read the data from the specified data source.

In our model the implementation looks like this:

.. image:: images/data-exchange-3.png
   :scale: 70
   :align: center

If this procedure is run successfully you will see that the data from the data source is imported as specified in the mapping file:

.. image:: images/data-exchange-4.png
   :scale: 70
   :align: center

This is the most basic setup for integrating and using the Data Exchange Library in your model. 



.. spelling::

    dex